import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  num_classes = W.shape[1]
  num_train = X.shape[0]

  for i in xrange(num_train):
    scores = X[i].dot(W)
    loss += -np.log(np.exp(scores[y[i]])/np.sum(np.exp(scores)))
    dW[:,y[i]] += -X[i]
    for j in xrange(num_classes):
      dW[:,j] += X[i]*np.exp(scores[j])/np.sum(np.exp(scores))
      # if j == y[i]:
        

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################


  loss /= num_train
  dW /= num_train

  # Add regularization to the loss.
  loss += reg * np.sum(W * W)
  # Add regularization to the gradient
  dW += 2*reg*W

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  num_train = X.shape[0]

  scores = np.matmul(X,W)

  c = np.exp(-np.amax(scores))

  loss = -np.sum(np.log(np.exp(scores[(np.array(list(range(len(y)))),y)] + c)/np.sum(np.exp(scores + c),axis = 1)))/scores.shape[0]
  loss += reg * np.sum(W * W)

  qq = np.zeros([num_train,W.shape[1]])
  qq[(np.array(list(range(len(y)))),y)] = 1

  pp = np.sum(np.exp(scores), axis=1)

  dW = np.matmul(X.T,np.exp(scores)/pp[:,np.newaxis]) - np.matmul(X.T,qq)
  dW /= num_train
  dW += 2*reg*W 

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  # pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

