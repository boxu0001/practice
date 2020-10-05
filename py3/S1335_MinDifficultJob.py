'''
1335. Minimum Difficulty of a Job Schedule
Hard

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

 
Example 1:

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 

Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15

Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843
'''

from __future__ import annotations

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        m=len(jobDifficulty)
        if m == 0 or d == 0 or d > m:
            return -1
        fmax = [[0]*m for _ in range(m)]    #fmax[i][j]: max of [i ~ j], inclusive index
        fdm = [[None]*m for _ in range(d+1)]    #fdm[di][mi]: di days end on mi_th job, fdm[1][mi] means day one finish on mi_th job 
        for i in range(m):
            for delta in range(m-i):
                if delta == 0:
                    fmax[i][i+delta] = jobDifficulty[i]
                else:
                    fmax[i][i+delta] = max(fmax[i][i+delta-1], jobDifficulty[i+delta])
        
        for mi in range(m):
            fdm[1][mi] = fmax[0][mi]    #fdm[1][mi] means day one finish on mi_th job , so it's the max from [0 ~ mi]
        
        # 注意这里数组的下标， di是表示用几天， mi是表示完成第几个job (index), m是总共多少个job
        for di in range(2, d+1):  #deduce next possible minimal, and find fmd(d, m-1) finally, 
            for mi in range(di-1, m-d+di):  # mi+1 >= di && m-mi-1 >= d-di ===>     di-1 <= mi < m -d +di
                for ki in range(di-2, mi):  # fdm(di, mi) = min(fdm(di, ki) , ki 在(di-2, mi] 之间， 因为 ki 要能被 di-1分开
                    if not fdm[di][mi]:
                        fdm[di][mi] = fdm[di-1][ki] + fmax[ki+1][mi]
                    else:
                        fdm[di][mi] = min(fdm[di][mi], fdm[di-1][ki] + fmax[ki+1][mi])    # ki range in [di-2 ~ mi)

        return fdm[d][m-1]
# D total days, M number of jobs
# di <= mi+1, D - di <= M - mi -1 ====>  di-1 <= mi < M - D + di
# 当 ddi = di - 1, 带入 得  ====> ddi <= ki < M - D + ddi  ===> di-2 <= ki < mi <= M-D+di-1


s=Solution()
s.minDifficulty([6,5,4,3,2,1],2)