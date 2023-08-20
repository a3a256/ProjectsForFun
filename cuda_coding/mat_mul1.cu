#include <cuda_runtime.h>
#include <device_launch_parameters.h>
#include <stdio.h>

cudaError_t matmul(int* c, int* a, int* b, int size[4], dim3 threads, dim3 blocks);

__global__ void mulKernel(int* c, int* a, int* b, int M, int N, int cols) {
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	int col = blockIdx.x * blockDim.x + threadIdx.x;
	if (row < M && col < N) {
		int tmp = 0;
		for (int i = 0; i < cols; i++) {
			tmp += a[N * row + i] * b[N * i + col];
		}
		c[N * row + col] = tmp;
	}
}

int main() {
	const int m = 2;
	const int n = 3;
	int a2d[m][n] = { {4, 2, 3}, {5, 1, 6} };
	int b2d[n][m] = { {6, 6}, {7, 2}, {3,9} };
	int a[m * n];
	int b[n * m];
	int i, j, k;
	k = 0;
	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			a[k] = a2d[i][j];
			printf("%d ", a[k]);
			k++;
		}
		printf("\n");
	}
	k = 0;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			b[k] = b2d[i][j];
			printf("%d ", b[k]);
			k++;
		}
		printf("\n");
	}
	int c[m * m] = { 0 };

	int threads = 2;
	int blocks = (m*m + threads - 1) / threads;
	dim3 THREADS(threads, threads);
	dim3 BLOCKS(blocks, blocks);
	int dim[4] = { m, n, n, m };
	cudaError_t status = matmul(c, a, b, dim, THREADS, BLOCKS);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed\n");
		return 1;
	}

	k = 0;
	for (i = 0; i < m; i++) {
		for (j = 0; j < m; j++) {
			printf("%d ", c[k]);
			k++;
		}
		printf("\n");
	}

	status = cudaDeviceReset();
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to reset the device\n");
		return 1;
	}

	return 0;
}

cudaError_t matmul(int* c, int* a, int* b, int size[4], dim3 threads, dim3 blocks) {
	int* dev_a = 0;
	int* dev_b = 0;
	int* dev_c = 0;
	cudaError_t status;

	status = cudaSetDevice(0);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to set a device\n");
		goto Error;
	}

	status = cudaMalloc((void**)&dev_a, size[0]*size[1] * sizeof(int));
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to allocate memory\n");
		goto Error;
	}
	status = cudaMalloc((void**)&dev_b, size[2] * size[3] * sizeof(int));
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to allocate memory\n");
		goto Error;
	}
	status = cudaMalloc((void**)&dev_c, size[0] * size[3] * sizeof(int));
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to allocate memory\n");
		goto Error;
	}

	status = cudaMemcpy(dev_a, a, size[0] * size[1] * sizeof(int), cudaMemcpyHostToDevice);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to copy from host to GPU buffer\n");
		goto Error;
	}
	status = cudaMemcpy(dev_b, b, size[2] * size[3] * sizeof(int), cudaMemcpyHostToDevice);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to copy from host to GPU buffer\n");
		goto Error;
	}

	mulKernel<<<blocks, threads>>>(dev_c, dev_a, dev_b, size[0], size[3], size[1]);

	status = cudaGetLastError();
	if (status != cudaSuccess) {
		fprintf(stderr, "Last error message %s\n", cudaGetErrorString(status));
		goto Error;
	}

	status = cudaDeviceSynchronize();
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to synchronize deivce \n");
		goto Error;
	}

	status = cudaMemcpy(c, dev_c, size[0] * size[3] * sizeof(int), cudaMemcpyDeviceToHost);
	if (status != cudaSuccess) {
		fprintf(stderr, "Failed to copy from GPU buffer to host\n");
		goto Error;
	}

Error:
	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_c);
	return status;
}