'''
Solving the Percolation Problem
'''

from QuickSort import QF

class Percolation(QF):
    '''creates n by n grid with all sites blocked'''
    def __init__(self, N) -> None:
        self.N = N
        self.grid = [i for i in range(N)]
        self.id = [i for i in range(N)]
        self.sz = [0 for i in range(N)]
        self.state = [0 for i in range(N)]

        # add top site to id list
        self.vtop_site = N + 1
        self.id.append(self.vtop_site)
        # add bottom site id to list
        self.vbot_site = N + 2
        self.id.append(self.vbot_site)

        # set top row id to id of top site
        for site in self.grid:
            if site // N == 0:
                self.union(site, self.vtop_site)
        # set bottom row id to id of bottom site
        for site in self.grid:
            if site // N == (N - 1):
                self.union(site, self.vbot_site)

    # opens site(r, c) if not opened
    def open(self, site:int):
        # connect site to open site near it
        corners = [0, self.N - 1, self.N * (self.N - 1), (self.N ** 2) - 1]
        if self.state[site] == 0:
            self.state[site] = 1
            #  top left corner
            if site == corners[0]:
                self.union(site, site + 1)
                self.union(site, site + self.N)

            #  top right corner
            if site == corners[1]:
                self.union(site, site - 1)
                self.union(site, site + self.N)

            #  bottom left corner
            if site == corners[2]:
                self.union(site, site + 1)
                self.union(site, site - self.N)

            #  bottom right corner
            if site == corners[3]:
                self.union(site, site - 1)
                self.union(site, site - self.N)

            #  left edge cases
            if site % self.N == 0 and site not in corners:
                self.union(site, site + self.N)
                self.union(site, site + 1)
                self.union(site, site - self.N)

            #  right edge cases
            if site % self.N == (self.N - 1) and site not in corners:
                self.union(site, site + self.N)
                self.union(site, site - 1)
                self.union(site, site - self.N)

            #  top edge cases
            if site // self.N == 0 and site not in corners:
                self.union(site, site + self.N)
                self.union(site, site + 1)
                self.union(site, site - 1)

            #  bottom edge cases
            if site // self.N == (self.N - 1) and site not in corners:
                self.union(site, site - self.N)
                self.union(site, site + 1)
                self.union(site, site - 1)

    # is site open?
    def is_open(self, site:int):
        return self.state[site] == 1

    # is site full?
    def is_full(self, site:int):
        # is site connected to top site?
        return self.root[site] == self.vtop_site

    # num of open sites
    def num_of_openSites(self):
        count = 0
        for i in self.state:
            if self.state[i] == 1:
                count += 1
        return count

    # does system percolate?
    def percolates(self):
        # is top virtual site connected to bottom virtual site?
        return(self.is_connected(self.vbot_site, self.vtop_site))



class PercolationStats:
    # perform independent trial on n-by-n grid
    def __init__(self, N:int, trials:int) -> None:
        pass

    # sample mean of the percolation threshold
    def mean(self):
        pass

    # sample standard deviation of percolation threshold
    def stddev(self):
        pass

    # low endpoint of 95% confidence interval
    def confidence_lo(self):
        pass

    # high endpoint of 95% confidence interval
    def confidence_hi(self):
        pass
