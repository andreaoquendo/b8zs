# Authors:
# Andrea Alexandra Sánez Oquendo
# Fernanda Rocha Costa Neto

class B8ZS:
    def __init__(self):
        pass

    ## Encodes to B8ZS
    def encode(self, signal):
        ami_signal = self.__ami(signal) # ami encoding
        return self.__violation_bipolar(ami_signal)

    ## Decodes from B8ZS
    def decode(self, digital_signal):
        ami_signal = self.__undo_violation(digital_signal)
        return self.__undo_ami(ami_signal)

    ## Synchronous clock encoding technique that uses bipolar pulses to represent logical 1.
    @staticmethod
    def __ami(bits):
        up = True
        digital_signal = []
        for bit in bits:
            if bit == 1:
                if up:
                    digital_signal.append(1)
                else:
                    digital_signal.append(2) #setup temporario
                up = not up
            else:
                digital_signal.append(0)
        return digital_signal

    ## Replaces 8 consecutive 0's into a double violation
    @staticmethod
    def __violation_bipolar(digital_signal):
        
        violation = '00000000'
        signal = ''.join(str(i) for i in digital_signal)

        # it's easier to get the violation using strings
        while violation in signal:
            i = signal.index(violation)
            if signal[i - 1] == '1':
                response = '00012021'
            else:
                response = '00021012'
            
            signal = signal.replace(violation, response, 1)

        let_to_num = {'0': 0, '1': 1, '2': -1}
        new_signal = [let_to_num[i] for i in signal]
        
        return new_signal

    ## Replaces violation by 8 consecutive 0's
    @staticmethod
    def __undo_violation(digital_signal):
        signal = [2 if x==-1 else x for x in digital_signal]
        signal = ''.join(str(i) for i in signal)
        
        signal = signal.replace('00012021', '00000000')
        signal = signal.replace('00021012', '00000000')

        let_to_num = {'0': 0, '1': 1, '2': -1}
        
        return [let_to_num[i] for i in signal]

    @staticmethod
    def __undo_ami(ami_signal):
        return [1 if x==-1 else x for x in ami_signal]

    ## Transforms the signal's format from list to string, replacing -1's by 2's
    @staticmethod
    def signal_to_string(signal):
        signal = [2 if x==-1 else x for x in signal]
        signal_string = ''.join([str(item) for item in signal])
        return signal_string

    ## Transforms the signal's format from string to list, replacing 2's by -1's
    @staticmethod
    def string_to_signal(word):
        letToNum = {'0': 0, '1': 1, '2': -1} 
        return [letToNum[i] for i in word]

        



