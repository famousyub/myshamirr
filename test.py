

from shamirsharesecret import SSS


'''
    Generate shares from a key
'''
sss = SSS(13, 17, 5, 3)
print("x = " + str(sss.choose_x()))
print("y = " + str(sss.generate_shares()))
# manual test
print("The key is " + str(sss.reconstruct_key([1, 3, 5], [8, 10, 11])))  # must return 13
# Calculate the share for different x
print("The share for x=1 is " + str(sss.calculate_y(1, [0,3,5], [sss.k, 10, 11])))
print("The share for x=3 is " + str(sss.calculate_y(3, [0,1,5], [sss.k, 8, 11])))
print("The share for x=5 is " + str(sss.calculate_y(5, [0,1,3], [sss.k, 8, 10])))

sss = SSS(1234, 1613, 6, 3)
print("x = " + str(sss.choose_x()))
print("y = " + str(sss.generate_shares()))
# manual test
print("The key is " + str(sss.reconstruct_key([1, 2, 3], [1494, 329, 965])))  # must return 1234
# Calculate the share for different x
print("The share for x=1 is " + str(sss.calculate_y(1, [0,2,3], [sss.k, 329, 965])))
print("The share for x=2 is " + str(sss.calculate_y(2, [0,1,3], [sss.k, 1494, 965])))
print("The share for x=3 is " + str(sss.calculate_y(3, [0,1,2], [sss.k, 1494, 329])))

sss = SSS(31318, 31847, 10, 5)
print("x = " + str(sss.choose_x()))
print("y = " + str(sss.generate_shares()))
# manual test
print(sss.reconstruct_key([413, 432, 451, 470, 489], [25439, 14847, 24780, 5910, 12734]))
print(sss.reconstruct_key([584, 432, 451, 470, 489], [21462, 14847, 24780, 5910, 12734]))
print(sss.reconstruct_key([584, 413, 565, 546, 489], [21462, 25439, 20806, 28578, 12734]))
print(sss.reconstruct_key([489, 565, 451, 470, 527], [12734, 20806, 24780, 5910, 12555]))
print(sss.reconstruct_key([508, 432, 584, 470, 489], [12492, 14847, 21462, 5910, 12734]))
# Calculate the share for different x
print("The share for x=413 is " + str(sss.calculate_y(413, [0, 432, 451, 470, 489], [sss.k, 14847, 24780, 5910, 12734])))
print("The share for x=584 is " + str(sss.calculate_y(584, [413, 432, 451, 470, 489], [25439, 14847, 24780, 5910, 12734])))
print("The share for x=508 is " + str(sss.calculate_y(508, [489, 565, 451, 470, 527], [12734, 20806, 24780, 5910, 12555])))
print("The share for x=0 is " + str(sss.calculate_y(0, [413, 432, 451, 470, 489], [25439, 14847, 24780, 5910, 12734])))

'''
    Share verification
'''

sss = SSS(1234, 94875355691, 9, 5)
x = [11, 22, 33, 44, 55, 66, 77, 88, 99]
y = [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987]
print(sss.reconstruct_key([11, 22, 33, 44, 55],[537048626, 89894377870, 65321160237, 18374404957, 24564576435]))
print(sss.reconstruct_key([22, 33, 44, 55, 66],[89894377870, 65321160237, 18374404957, 24564576435, 87371334299]))
print(sss.reconstruct_key([33, 44, 55, 66, 77],[65321160237, 18374404957, 24564576435, 87371334299, 60461341922]))
print(sss.reconstruct_key([44, 55, 66, 77, 88],[18374404957, 24564576435, 87371334299, 60461341922, 10096524973]))
print(sss.reconstruct_key([55, 66, 77, 88, 99],[24564576435, 87371334299, 60461341922, 10096524973, 81367619987]))
print(sss.reconstruct_key([11, 22, 33, 44, 55, 66, 77, 88, 99], [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987]))
print(sss.reconstruct_key([22, 33, 44, 55, 66, 77, 88, 99], [89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987]))
print(sss.reconstruct_key([11, 22, 33, 44, 55, 66, 77, 88], [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973]))

if sss.validate_shares(x, y):
    print("Shares are valid")
else:
    print("Shares are not valid")
    print("The defective share is " + str(sss.find_defective_share([11, 22, 33, 44, 55, 66, 77, 88, 99], [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987])))