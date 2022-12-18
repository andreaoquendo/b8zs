class B8ZS:
    def __init__(self):
        self.bits = []
        self.digitalSignal = []

    def encode(self, bits):
        self.bits = bits
        self.digitalSignal = []
        self.ami()
        self.violationBipolar()
        return self.digitalSignal

    def decode(self, signal):
        self.digitalSignal = signal
        self.bits = []
        self.undoViolation()
        self.undoAMI()
        
        return self.bits

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

    def violationBipolar(self):
        count = 0
        violation = '00000000'
        signal = ''.join(str(i) for i in self.digitalSignal)

        while violation in signal:
            i = signal.index(violation)
            if signal[i - 1] == '1':
                response = '00012021'
            else:
                response = '00021012'
            
            signal = signal.replace(violation, response, 1)
        
        newSignal = []

        letToNum = {'0': 0, '1': 1, '2': -1} 
        for i in signal:
            newSignal.append(letToNum[i])
        
        self.digitalSignal = newSignal
            
    def undoViolation(self):
        signal = [2 if x==-1 else x for x in self.digitalSignal]
        signal = ''.join(str(i) for i in signal)
        
        violation1 = '00012021'
        violation2 = '00021012'
        response = '00000000'
        
        signal = signal.replace(violation1, response)
        signal = signal.replace(violation2, response)
        
        newSignal = []

        letToNum = {'0': 0, '1': 1, '2': -1} 
        for i in signal:
            newSignal.append(letToNum[i])
        
        self.digitalSignal = newSignal

    def undoAMI(self):
        signal = [1 if x==-1 else x for x in self.digitalSignal]
        self.bits = signal

        



