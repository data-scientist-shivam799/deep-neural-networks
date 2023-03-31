# Coded by Shivam Kumar
# PRN: 20190802073

import tensorflow as tf

class Tensorflow:
    def __init__(self):
        print(tf.__version__)
    def addition(self):
        firstTensor=tf.constant([1,2,3],tf.int32,name='firstTensor')
        secondTensor=tf.constant([3,2,1],tf.int32,name='secondTensor')
        result=tf.add(firstTensor,secondTensor)
        print("\nResult of addition is",result)
    def subtraction(self):
        thirdTensor=tf.constant([[2,3,5],[1,6,8],[0,7,9]],tf.int32,name='thirdTensor')
        fourthTensor=tf.constant([[4,0,8],[1,2,6],[2,6,3]],tf.int32,name='fourthTensor')
        result=tf.subtract(thirdTensor,fourthTensor)
        print("\nResult of substraction is",result)
    def multipy(self):
        mulTensor1=tf.constant([[2,2,2],[1,6,3]],tf.int32,name='mulTensor1')
        mulTensor2=tf.constant([[6,6,6],[0,0,0]],tf.int32,name='mulTensor2')
        result=tf.multiply(mulTensor1,mulTensor2)
        print("\nResult of multiplication is",result)
    def division(self):
        divTen1=tf.constant([[6,2],[2,1]],tf.int32,name='divTen1')
        divTen2=tf.constant([[1,1],[1,1]],tf.int32,name='divTen2')
        result=tf.truediv(divTen1,divTen2)
        print("\nResult of division is",result)
    def exponent(self):
        expTen1=tf.constant([1,2],dtype=tf.float32)
        expTen2=tf.constant([2,3],dtype=tf.float32)
        result=tf.exp(expTen1,expTen2)
        print("\nResult of exponent is",result)
    def sqroot(self):
        sqroot=tf.constant([4,2,16],dtype=tf.float32,name='sqroot')
        result=tf.sqrt(sqroot)
        print("\nResult of sqroot is",result)
    def pow(self):
        powTen1=tf.constant([1,2,3],dtype=tf.float32,name='powTen1')
        powTen2=tf.constant([1,0,2],dtype=tf.float32,name='firstTensor')
        result=tf.pow(powTen1,powTen2)
        print("\nResult of power is",result)

def main():
    appRunner=Tensorflow()
    appRunner.addition()
    appRunner.subtraction()
    appRunner.multipy()
    appRunner.division()
    appRunner.sqroot()
    appRunner.exponent()
    appRunner.pow()

if __name__=="__main__":
    main()