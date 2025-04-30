class Result():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getting_result(self):
        sum=0
        for i in self.marks:
            sum+=i
        avg=sum/len(self.marks)
        return avg

    
abir=Result('Abir',[80,90,100])
result=abir.getting_result()
print(result)