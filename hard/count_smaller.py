class Solution:

    def merge(self, arr1, arr2, out):
        x = []
        i1 = 0
        i2 = 0
        l1 = len(arr1)
        l2 = len(arr2)

        while i1 < l1 and i2 < l2:
        
            if arr1[i1][0] > arr2[i2][0]:
                if arr1[i1][1] < arr2[i2][1]:
                    out[arr1[i1][1]] += len(arr2) - i2
                x.append(arr1[i1])
                i1 += 1
            else:
                if arr2[i2][1] < arr1[i1][1]:
                    out[arr2[i2][1]] += len(arr1) - i1
                x.append(arr2[i2])
                i2 += 1
        
        x += arr1[i1:]
        x += arr2[i2:]
        return x


    def mergeSort(self, arr, out):

        if len(arr) == 1:
            return arr
        
        m = len(arr) // 2
        arr1 = arr[:m]
        arr2 = arr[m:]

        arr1 = self.mergeSort(arr1, out)
        arr2 = self.mergeSort(arr2, out)

        out = self.merge(arr1, arr2, out)
        return out

    def countSmaller(self, nums):
        arr = [[nums[i], i] for i in range(len(nums))]
        out = [0 for i in range(len(nums))]


        arr = self.mergeSort(arr, out)

        print(out)
        return out
