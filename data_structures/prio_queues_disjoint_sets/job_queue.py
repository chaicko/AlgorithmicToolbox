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
        assert m == len(self._jobs)
        self.__init__(n, jobs)

    def write_response(self):
        for i in range(len(self._jobs)):
            print(self._assigned_workers[i], self._start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        next_free_time = [0] * self._num_workers
        for i in range(len(self._jobs)):
            next_worker = 0
            for j in range(self._num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self._assigned_workers[i] = next_worker
            self._start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self._jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
