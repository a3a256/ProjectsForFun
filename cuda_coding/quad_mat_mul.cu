#include <cuda_runtime.h>
#include <device_launch_parameters.h>

#include <stdio.h>

cudaError_t MatMul(int* c, int* a, int* b, unsigned int size, int m, int n, dim3 THREADS, dim3 BLOCKS);

__global__ void multKernel(int* c, int* a, int* b, int N) {
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	int col = blockIdx.x * blockDim.x + threadIdx.x;
	if (row < N && col < N) {
		int tmp = 0;
		for (int i = 0; i < N; i++) {
			tmp += a[N * row + i] * b[N * i + col];
		}
		c[N * row + col] = tmp;
		printf("%d, %d = %d\n", row ,col, tmp);
	}
}

int main() {
	const int m = 2, n = 2;
	const int size = m * n;
	int i, j, k;
	int one2d[m][n] = { {6, 4}, {7, 7} };
	int two2d[m][n] = { {2, 9}, {4, 6} };
	int one[size];
	int two[size];
	k = 0;
	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			one[k] = one2d[i][j];
			two[k] = two2d[i][j];
			k++;
		}
	}
	int res[size] = { 0 };
	int threads = 1;
	int blocks = (size + threads - 1) / threads;
	dim3 THREADS(threads, threads);
	dim3 BLOCKS(blocks, blocks);
	cudaError_t status = MatMul(res, one, two, size, m, n, THREADS, BLOCKS);

	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to multiple quadratic matrix\n");
		return 1;
	}
	k = 0;
	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			printf("%d ", res[k]);
			k++;
		}
		printf("\n");
	}

	status = cudaDeviceReset();
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to reset CUDA device\n");
		return 1;
	}

	return 0;
}


cudaError_t MatMul(int* c, int* a, int* b, unsigned int size, int m, int n, dim3 THREADS, dim3 BLOCKS) {
	int* dev_a = 0;
	int* dev_b = 0;
	int* dev_c = 0;
	cudaError_t status;

	status = cudaSetDevice(0);
	if (status != cudaSuccess) {
		fprintf(stderr, "CUDA device not found\n");
		goto Error;
	}

	status = cudaMalloc((void**)&dev_a, size * sizeof(int));
	if (status != cudaSuccess) {
		fprintf(stderr, "Memory allocation error\n");
		goto Error;
	}
	status = cudaMalloc((void**)&dev_b, size * sizeof(int));
	if (status != cudaSuccess) {
		fprintf(stderr, "Memory allocation error\n");
		goto Error;
	}
	status = cudaMalloc((void**)&dev_c, size * sizeof(int));
	if (status != cudaSuccess) {
		fprintf(stderr, "Memory allocation error\n");
		goto Error;
	}

	status = cudaMemcpy(dev_a, a, size * sizeof(int), cudaMemcpyHostToDevice);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to copy from host to GPU buffer\n");
		goto Error;
	}
	status = cudaMemcpy(dev_b, b, size * sizeof(int), cudaMemcpyHostToDevice);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to copy from host to GPU buffer\n");
		goto Error;
	}

	multKernel<<<BLOCKS,THREADS>>>(dev_c, dev_a, dev_b, m);

	status = cudaGetLastError();
	if (status != cudaSuccess) {
		fprintf(stderr, "Error: %s \n", cudaGetErrorString(status));
		goto Error;
	}

	status = cudaDeviceSynchronize();
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to synchronize device, error no. :%d\n", status);
		goto Error;
	}

	status = cudaMemcpy(c, dev_c, size * sizeof(int), cudaMemcpyDeviceToHost);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to copy from GPU buffer to host array\n");
		goto Error;
	}

Error:
	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_b);
	return status;
}
