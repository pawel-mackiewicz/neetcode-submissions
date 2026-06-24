class UnionFind:
    def __init__(self):
        self.par = {}
        self.weights = {}

    def find(self, email: str) -> str:
        while email != self.par[email]:
            self.par[email] = self.par[self.par[email]]
            email = self.par[email]
        return email
    
    def union(self, e1: str, e2: str = ""):
        if e2 == "":
            self.par[e1] = e1
            return

        if e1 not in self.par:
            self.par[e1] = e1
            self.weights[e1] = 0
        if e2 not in self.par:
            self.par[e2] = e2
            self.weights[e2] = 0

        p1 = self.find(e1)
        p2 = self.find(e2)

        if self.weights[p1] > self.weights[p2]:
            self.par[p2] = p1
        elif self.weights[p1] < self.weights[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.weights[p2] += 1
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        emailNames = {}

        for account in accounts:
            name = account[0]
            e1 = account[1]
            emailNames[e1] = name
            if len(account) == 2:
                uf.union(e1)
            for i in range(2,len(account)):
                e2 = account[i]
                emailNames[e2] = name
                uf.union(e1,e2)

        emails = {}
        for email in emailNames.keys():
            parent = uf.find(email)

            if parent not in emails:
                emails[parent] = [email]
            else:
                emails[parent].append(email)
        
        res = []

        for parent, emails in emails.items():
            name = emailNames[parent]
            emails.sort()
            acc = [name]
            acc += emails
            res.append(acc)
        
        return res