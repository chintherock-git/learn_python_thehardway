class Book:
    def __init__(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"Book Title is {self.name} and Book Author is{self.author}"   
    
    def __del__(self):
        del self 
        
if __name__=="__main__":
    b= ("Phoenix Project","Gene Kim",2000)
    print(len(b))
    print(b)
    del b
    
    
