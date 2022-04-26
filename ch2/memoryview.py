# 마치 c의 강제 형변환 
import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) # 정수형
memv = memoryview(numbers) # memory view 객체 생성
print( len(memv) )
print( memv[0] ) 
memv_oct = memv.cast('B') # unsigned char 로 형변환
print( memv_oct.tolist() ) #
memv_oct[5] = 4
print( numbers )

