from copy import copy

class Bot():
    def __init__(self,depth, maximizingPlayer:bool,evaluate,branchSize=10,branchDecreaseDepth=1):
        self.depth=depth
        self.maximizingPlayer=maximizingPlayer
        self.evaluate=evaluate
        self.branchSize=branchSize
        self.branchDecreaseDepth=branchDecreaseDepth

    def getChildren(self,position,maximizingPlayer,depth):
        children = []
        for move in position.legal_moves:
            newPosition = copy(position)
            newPosition.push(move)
            if depth>self.branchDecreaseDepth and self.branchDecreaseDepth!=0:
                children.append((newPosition, move,self.minimax(newPosition,self.branchDecreaseDepth,not maximizingPlayer)[0]))
            else:
                children.append((newPosition, move,0))
        if depth > self.branchDecreaseDepth and self.branchDecreaseDepth != 0:
            return sorted(children, key=lambda child: child[2], reverse=maximizingPlayer)[0:min(self.branchSize, len(children))]
        else:
            return children

    def getMove(self,position):
        self.transPositionTable = {}
        return self.minimax(position,self.depth,self.maximizingPlayer)

    def minimax(self,position,depth, maximizingPlayer, alpha=-10000, beta=10000):
        if depth == 0:
            return self.evaluate(position), None
        if maximizingPlayer:
            maxValue = -10000
            bestMove = None
            for child, move,_ in self.getChildren(position,maximizingPlayer,depth):
                value, _ = self.minimax(child, depth - 1, False,alpha=alpha,beta=beta)
                if depth==6:
                    print(move,value,_,bestMove,maxValue)
                if value > maxValue:
                    maxValue = value
                    bestMove = move
                alpha = max(alpha, value)
                if value>=beta:
                    break
            return maxValue, bestMove
        else:
            minValue = 10000
            bestMove = None
            for child, move,_ in self.getChildren(position,maximizingPlayer,depth):
                value, _ = self.minimax(child, depth - 1, True,alpha=alpha,beta=beta)
                if depth==6:
                    print(move,value,_,bestMove,minValue)
                if value < minValue:
                    minValue = value
                    bestMove = move
                beta = min(beta, value)
                if value <= alpha:
                    break
            return minValue, bestMove

