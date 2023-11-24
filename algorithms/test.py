site = 57
N = 5
def union(p, q):
    pass
#  FOUR CORNER CASES
corners = [0, N - 1, N * (N - 1), (N ** 2) - 1]
#  top left corner
if site == 0:
    union(site, site + 1)
    union(site, site + N)

#  top right corner
if site == (N - 1):
    union(site, site - 1)
    union(site, site + N)

#  bottom left corner
if site == (N * (N -1)):
    union(site, site + 1)
    union(site, site - N)

#  bottom right corner
if site == ((N ** 2) - 1):
    union(site, site - 1)
    union(site, site - N)

#  left edge cases
if site % N == 0 and site not in corners:
    union(site, site + N)
    union(site, site + 1)
    union(site, site - N)

#  right edge cases
if site % N == (N - 1) and site not in corners:
    union(site, site + N)
    union(site, site - 1)
    union(site, site - N)

#  top edge cases
if site // N == 0 and site not in corners:
    union(site, site + N)
    union(site, site + 1)
    union(site, site - 1)

#  bottom edge cases
if site // N == (N - 1) and site not in corners:
    union(site, site - N)
    union(site, site + 1)
    union(site, site - 1)

print(corners)