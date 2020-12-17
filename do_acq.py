import un0usb as USB
import datetime

fpga = USB.FpgaControl('ftdi://ftdi:2232:/', spi_freq=8E6)
fpga.reload()
fpga.reset()

gain = [(0*x) for x in range(32)]
gain[0] = 0
fpga.do_acquisition(acq_lines=32, gain=gain, double_rate=True)
now = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
#print(now)
file = fpga.save(nameFile = str(now)+"_ndt")
plot = USB.FView()
data = plot.readfile(file)
plot.plotNDT(data,fCentral=2.5,bandwidth=0.6)

