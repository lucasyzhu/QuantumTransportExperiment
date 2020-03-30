## GS610

实验室暂时只把GS610作为电压源来使用。手动操作可以参考GS210的说明。

**Range**: 0.2 2 12 20 30 60 110 (V)



#### VISA 示例

```python
import visa
import time


address = "GPIB0::2::INSTR"
inst = visa.ResourceManager().open_resource(address, read_termination='\n')

#check connection status
command = "*IDN?"
return_str = inst.query(command)
print(return_str)

rng     = 2
command = ":SOUR:VOLT:RANG " + str(rng)
inst.write(command)
error_info = inst.query(":SYST:ERR?")
print(error_info)

voltage = 1.11
command = ":SOUR:VOLT:LEV "+ str(voltage) + ";:OUTP ON"
inst.write(command)
error_info = inst.query(":SYST:ERR?")
print(error_info)

inst.close() #close visa

```

