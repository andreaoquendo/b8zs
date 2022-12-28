# Authors:
# Andrea Alexandra Sánez Oquendo
# Fernanda Rocha Costa Neto

class B8ZS:
    def __init__(self):
        self.bits = [] # original signal
        self.digitalSignal = []

    
    def encode(self, bits):
        # cleans auxiliar list
        self.digitalSignal.clear()

        self.bits = bits
        self.ami()
        self.violationBipolar()
        return self.digitalSignal

    def decode(self, signal):
        self.digitalSignal = signal
        self.bits.clear()
        self.undoViolation()
        self.undoAMI()
        
        return self.bits

    ### AMI (Alternate Mark Inversion)
    ### Parameters: None
    ### Description: Synchronous clock encoding technique that uses bipolar pulses to represent logical 1.
    def ami(self):
        up = True
        for bit in self.bits:
            if bit == 1:
                if up:
                    self.digitalSignal.append(1)
                else:
                    self.digitalSignal.append(2) #setup temporario
                up = not up
            else:
                self.digitalSignal.append(0)

    ## Bipolar Violation of AMI
    ## Parameters: None
    ## Description: Replaces 8 consecutive 0's into a double violation
    def violationBipolar(self):
        
        violation = '00000000'
        signal = ''.join(str(i) for i in self.digitalSignal)

        # it's easier to get the violation using strings
        while violation in signal:
            i = signal.index(violation)
            if signal[i - 1] == '1':
                response = '00012021'
            else:
                response = '00021012'
            
            signal = signal.replace(violation, response, 1)

        letToNum = {'0': 0, '1': 1, '2': -1}
        newSignal = [letToNum[i] for i in signal]
        
        self.digitalSignal = newSignal

    ## Undoes Bipolar Violation of AMI
    ## Parameters: None
    ## Description: Replaces violation by 8 consecutive 0's
    def undoViolation(self):
        signal = [2 if x==-1 else x for x in self.digitalSignal]
        signal = ''.join(str(i) for i in signal)
        
        violation1 = '00012021'
        violation2 = '00021012'
        response = '00000000'
        
        signal = signal.replace(violation1, response)
        signal = signal.replace(violation2, response)

        letToNum = {'0': 0, '1': 1, '2': -1}
        newSignal = [letToNum[i] for i in signal]
        
        self.digitalSignal = newSignal

    def undoAMI(self):
        signal = [1 if x==-1 else x for x in self.digitalSignal]
        self.bits = signal

        



