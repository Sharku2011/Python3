class bst:
    def __init__(self):
        self.root = None
    def insert(self):
        Data = input('이진트리에 추가할 데이터를 입력해 주세요 : ')
        if len(Data) == 0:
            print('잘못된 입력값입니다.')
        else:
            if self.root == None:
                self.root = bstNode(Data)
            else:
                self.root.insertNode(Data)
    def height(self):
        if self.root == None:
            return -1
        else:
            return self.root.height()
    def find(self):
        Data = input('찾을 데이터를 입력해 주세요 : ')
        if len(Data) == 0:
            print('잘못된 입력값입니다.')
        else:
            self.root.find(Data)
    def delete(self):
        Data = input('이진트리에서 제거할 데이터를 입력해 주세요 : ')
        if len(Data) == 0:
            print('잘못된 입력값입니다.')
        else:
            self.root.delete(Data)
    
class bstNode:
    def __init__(self,Data=None):
        self.data = Data
        self.parent = None
        self.left = None
        self.right = None
    def insertNode(self,Data):
        if self.data > Data:
            if self.left == None:
                newNode = bstNode(Data)
                newNode.parent = self
                self.left = newNode
            else:
                self.left.insertNode(Data)
        elif self.data < Data:
            if self.right == None:
                newNode = bstNode(Data)
                newNode.parent = self
                self.right = newNode
            else:
                self.right.insertNode(Data)
        else:
            print('{} 은/는 이미 해당 Tree 안에 존재합니다.'.format(Data))
    def height(self):
        if self.left != None:
            _left = self.left.height()
        else:
            _left =  -1
        if self.right != None:
            _right = self.right.height()
        else:
            _right = -1
        return 1+max(_left,_right)
    def find(self,Data):
        if self.data > Data:
            if self.left == None:
                print('{} 은/는 해당 Tree 안에 존재하지 않습니다.'.format(Data))
            else:
                self.left.find(Data)
        elif self.data < Data:
            if self.right == None:
                print('{} 은/는 해당 Tree 안에 존재하지 않습니다.'.format(Data))
            else:
                self.right.find(Data)
        else:
            depth = 0
            ptr = self
            while ptr.parent != None:
                ptr = ptr.parent
                depth += 1
            print('{} 을/를 찾았습니다.'.format(self.data))
            if self.parent != None:
                print('parent : {}'.format(self.parent.data))
            else:
                print('parent : None')
            if self.left != None:
                print('left : {}'.format(self.left.data))
            else:
                print('left : None')
            if self.right != None:
                print('right : {}'.format(self.right.data))
            else:
                print('right : None')
            print('depth : {}'.format(depth))
    def delete(self,Data):
        if self.data > Data:
            if self.left == None:
                print('{} 은/는 해당 Tree 안에 존재하지 않습니다.'.format(Data))
            else:
                self.left.delete(Data)
        elif self.data < Data:
            if self.right == None:
                print('{} 은/는 해당 Tree 안에 존재하지 않습니다.'.format(Data))
            else:
                self.right.delete(Data)
        else:
            if self.left != None and self.right == None:
                self.parent.left = self.left
                self.left.parent = self.parent
                del self
            elif self.left == None and self.right != None:
                self.parent.right = self.right
                self.right.parent = self.parent
                del self
            elif self.left != None and self.right != None:
                successor = self
                successor = successor.right
                while successor.left != None:
                    successor = successor.left
                self.data = successor.data
                self.right.left = successor.right
                successor.right.parent = self.right
                del successor
            print('{} 이/가 Tree에서 삭제되었습니다.'.format(Data))

#일단 유효한 값을 입력 받아야만 재귀함수가 실행될 수 있다.(None(Null)이나 [] 같은 경우 height 라는 메소드가 없기 때문에 위의 코드처럼
#None값에 대해서 재귀함수를 호출해야할 경우 논리 혹은 예외처리로 체크해준다.
#문자열만 비교하게 해뒀더니 숫자비교가 안된다. 수정할 것.
#showTree 어떻게 하지