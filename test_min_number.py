from clasiffier import min_number

def test_min_number():
	assert min_number([1,2,3,4,5,6,7,0]) == 0
	assert min_number([-2, -5, 5, -1]) == -5
	assert min_number([9, 18, 27, 36, 45, 54, 63, 72, 80]) == 9
