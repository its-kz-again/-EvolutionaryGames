import matplotlib.pyplot as plt
import json

with open("data.json", 'r+') as f:
    data = json.load(f)
    mini = list(map(int, data['min']))
    avg = list(map(float, data['avg']))
    maxi = list(map(int, data['max']))

ranges = list(range(len(mini)))
plt.xlabel('Generation')
plt.ylabel('Score')
plt.plot(ranges, mini, 'o-', label="min scores")
plt.plot(ranges, avg, 'o-', label="average scores")
plt.plot(ranges, maxi, 'o-', label="max scores")
plt.legend()
plt.show()