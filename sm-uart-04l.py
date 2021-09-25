import time
import serial

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout = 1)

def get_serial_number(ser):
	ser.reset_input_buffer()
	ser.write([0x20, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x53, 0x7A])
	reading = ser.read(20)

	ok_bytes = []
	for byte in reading:
		if byte > 0x2E:
			ok_bytes.append(chr(byte))

	if len(ok_bytes) < 18:
		return False

	return "".join(ok_bytes)

def get_default_output(ser):
	ser.reset_input_buffer()
	reading = ser.read(32)
	if len(reading) != 32 or reading[0] != 0x42 or reading[1] != 0x4D:
		return False

	crc_sum = 0
	for i in range(30):
		crc_sum += reading[i]

	if crc_sum != (reading[30] * 256 + reading[31]):
		return False

	return reading

def send_command(ser, cmd, data):
	request_bytes = [0x42, 0x4D, cmd, data[0], data[1]]

	# crc
	crc_sum = 0
	for request_byte in request_bytes:
		crc_sum += request_byte

	request_bytes.append(crc_sum >> 8)
	request_bytes.append(crc_sum & 0xFF)

	ser.write(request_bytes)

def send_get_reading_command(ser): # only needed for 'ask-answer' output mode
	send_command(ser, 0xE2, [0x00, 0x00])

def set_output_mode(ser, mode): # mode = 0x00 for 'ask-answer mode', 0x01 for 'direct output mode'
	send_command(ser, 0xE1, [0x00, mode])

def set_standby_control(ser, mode): # mode = 0x00 for 'standby mode', 0x01 for 'working mode'
	send_command(ser, 0xE4, [0x00, mode])


serial_number = None
for i in range(3):
	serial_number = get_serial_number(ser)
	if serial_number != False:
		break

print("Serial number: " + str(serial_number) + "\n")

print("PM1\tPM2.5\tPM10\tErrors")

while True:
	default_output = get_default_output(ser)
	if default_output != False:
		value_pm1   = ((default_output[4] & 0x3F) << 8) | default_output[5]
		value_pm2_5 = ((default_output[6] & 0x3F) << 8) | default_output[7]
		value_pm10  = ((default_output[8] & 0x3F) << 8) | default_output[9]

		error_byte = default_output[29]
		errors = []
		if error_byte & 0b00010000 != 0:
			errors.append("high temperature alarm")
		if error_byte & 0b00001000 != 0:
			errors.append("low temperature alarm")
		if error_byte & 0b00000100 != 0:
			errors.append("fan error")
		if len(errors) == 0:
			errors.append("no error")

		print("{0}\t{1}\t{2}\t{3}".format(value_pm1, value_pm2_5, value_pm10, ", ".join(errors)))
	else:
		print("no data")

	time.sleep(1)
