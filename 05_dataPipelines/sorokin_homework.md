Opposed to tuition, as we increase the number of threads the images / second tends to decrease. This is likely because the overhead of copying data to more cores outweighs the benefits of parallel processing. I would suspect that for less than 64 threads, increasing the threads provides a benefit as we saw in the in-class exercise. The buffer size of 8 outperforms the buffer size of 4 or 16. Optimally, we would choose around 64 threads (maybe less if further testing indicates better performance e.g. with 32 threads) and a prefetch buffer size of 8.

**Mean Images per Second**

|                         | 64 parallel_threads | 128 parallel_threads | 256 parallel_threads | 
| ----------------------- | ------------------- | -------------------- | -------------------- |
| prefetch_buffer_size 4  | 887                 | 772                  | 391                  |
| prefetch_buffer_size 8  | 860                 | 805                  | 655                  |
| prefetch_buffer_size 16 | 888                 | 765                  | 113                  |

**Standard Deviation Images per Second**

|                         | 64 parallel_threads | 128 parallel_threads | 256 parallel_threads | 
| ----------------------- | ------------------- | -------------------- | -------------------- |
| prefetch_buffer_size 4  | 114                 | 61                   | 64                   |
| prefetch_buffer_size 8  | 54                  | 92                   | 69                   |
| prefetch_buffer_size 16 | 124                 | 113                  | 49                   |
