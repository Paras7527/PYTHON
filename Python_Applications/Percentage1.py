def main():
    print("Enter Total Marks : ")
    Value1=int(input())
    
    print("Enter Obtained Marks : ")
    Value2=int(input())
    
    Percentage=((Value2 / Value1)*100)  #Business Logic

    print("Percentage is : ",Percentage)
    
if __name__=="__main__":
    main()