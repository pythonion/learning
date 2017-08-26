class Name:
    fn=""
    ln=""
    def __init__(self,fname,lname):
        self.fn = fname
        self.ln = lname
    def display(self):
        print "%s, %s" % (self.fn,self.ln)
