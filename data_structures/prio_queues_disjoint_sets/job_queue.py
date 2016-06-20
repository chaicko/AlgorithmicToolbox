# python3


class JobQueue:
    def __init__(self, num_workers=0, jobs=()):
        self._num_workers = num_workers
        self._jobs = list(jobs)
        self._assigned_workers = [None] * len(self._jobs)
        self._start_times = [None] * len(self._jobs)

    @property
    def num_workers(self):
        return self._num_workers

    @property
    def jobs(self):
        return self._jobs

    @property
    def start_times(self):
        return self._start_times

    @property
    def assigned_workers(self):
        return self._assigned_workers

    def read_data(self):
        n, m = map(int, input().split())
        jobs = list(map(int, input().split()))
        assert m == len(jobs)
        self.__init__(n, jobs)

    def write_response(self):
        for i in range(len(self._jobs)):
            print(self._assigned_workers[i], self._start_times[i])

    def assign_jobs(self):
        # Trivial case
        if len(self.jobs) <= self.num_workers:
            self._assigned_workers = [i for i in range(len(self._jobs))]
            self._start_times = [0] * len(self._jobs)
            return

        # Create Heap
        from collections import namedtuple
        import heapq
        MyThread = namedtuple('MyThread', 'start_time, id')
        heap = [MyThread(0, i) for i in range(self._num_workers)]
        heapq.heapify(heap)

        for i, job in enumerate(self._jobs):
            # Read the root contents
            sched_thread_id = heap[0].id
            sched_thread_start = heap[0].start_time
            # Append to output
            self._assigned_workers[i] = sched_thread_id
            self._start_times[i] = sched_thread_start
            # Update heap with next start time
            heapq.heapreplace(heap, MyThread(sched_thread_start + job, sched_thread_id))

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
