

def bucketSort(list):
    bucket = []

    # Create empty buckets
    for i in range(len(list)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in list:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(list)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(list)):
        for j in range(len(bucket[i])):
            list[k] = bucket[i][j]
            k += 1
    return list

list  =  [.23, .39, .31, .58, .67, .47, .51]
print(bucketSort(list))