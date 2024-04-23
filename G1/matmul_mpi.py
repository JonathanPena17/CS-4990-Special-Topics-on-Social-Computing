from mpi4py import MPI
import numpy as np
import sys
import time

def matmul_distributed(n):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Ensure the matrix size is divisible by the number of processors
    if n % size != 0:
        if rank == 0:
            print("Error: Matrix size must be divisible by the number of processors.")
        return

    local_size = n // size
    A_local = np.random.rand(local_size, n)
    B_local = np.random.rand(n, local_size)
    C_local = np.zeros((local_size, n))

    start_time = MPI.Wtime()

    # Perform the matrix multiplication
    for i in range(size):
        k = (rank + i) % size
        B_part = comm.bcast(B_local[:, local_size*k:local_size*(k+1)] if rank == k else one, root=k)
        C_local += np.dot(A_local, B_part)

    end_time = MPI.Wtime()
    time_taken = end_time - start_time

    if rank == 0:
        print(f"Runtime for n={n}, P={size}: {time_taken} seconds")
        return time_taken

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python matmul_mpi.py [matrix_size] [P]")
        sys.exit(1)

    n = int(sys.argv[1])
    P = int(sys.argv[2])  # This argument is actually not used directly.

    if MPI.COMM_WORLD.Get_size() != P:
        if MPI.COMM_WORLD.Get_rank() == 0:
            print(f"Error: The number of MPI processes ({MPI.COMM_WORLD.Get_size()}) does not match the requested P ({P}).")
        sys.exit(1)

    matmul_distributed(n)
