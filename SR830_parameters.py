def get_tau(comp):
    tau = int(comp.query('OFLT?'))
    if tau==0:
        return 10e-6
    elif tau==1:
        return 30e-6
    elif tau==2:
        return 100e-6
    elif tau==3:
        return 300e-6
    elif tau==4:
        return 1e-3
    elif tau==5:
        return 3e-3
    elif tau==6:
        return 10e-3
    elif tau==7:
        return 30e-3
    elif tau==8:
        return 100e-3
    elif tau==9:
        return 300e-3
    elif tau==10:
        return 1.0
    elif tau==11:
        return 3.0
    elif tau==12:
        return 10.0
    elif tau==13:
        return 30.0
    elif tau==14:
        return 100.0
    elif tau==15:
        return 300.0
    elif tau==16:
        return 1000.0
    elif tau==17:
        return 3000.0
    elif tau==18:
        return 10000.0
    elif tau==19:
        return 30000.0
    else:
        return 0
        
        
def set_tau(comp,tau_s):
    if tau_s==10e-6:
        tau_ind = 0
    elif tau_s==30e-6:
        tau_ind = 1
    elif tau_s==100e-6:
        tau_ind = 2
    elif tau_s==300e-6:
        tau_ind = 3
    elif tau_s==1e-3:
        tau_ind = 4
    elif tau_s==3e-3:
        tau_ind = 5
    elif tau_s==10e-3:
        tau_ind = 6
    elif tau_s==30e-3:
        tau_ind = 7
    elif tau_s==100e-3:
        tau_ind = 8
    elif tau_s==300e-3:
        tau_ind = 9
    elif tau_s==1.0:
        tau_ind = 10
    elif tau_s==3.0:
        tau_ind = 11
    elif tau_s==10.0:
        tau_ind = 12
    elif tau_s==30.0:
        tau_ind = 13
    elif tau_s==100.0:
        tau_ind = 14
    elif tau_s==300.0:
        tau_ind = 15
    elif tau_s==1000.0:
        tau_ind = 16
    elif tau_s==3000.0:
        tau_ind = 17
    elif tau_s==10000.0:
        tau_ind = 18
    elif tau_s==30000.0:
        tau_ind = 19
    else:
        print('invalid time constant defaulting to current time constant')
        tau_ind = int(comp.query('OFLT?'))
        
    comp.write('OFLT %d' % tau_ind)
    
    
def set_sampling_rate(comp, freq):
    if freq==0.0625:
        freq_ind = 0
    elif freq==0.125:
        freq_ind = 1
    elif freq==0.25:
        freq_ind = 2
    elif freq==0.5:
        freq_ind = 3
    elif freq==1:
        freq_ind = 4
    elif freq==2:
        freq_ind = 5    
    elif freq==4:
        freq_ind = 6
    elif freq==8:
        freq_ind = 7
    elif freq==16:
        freq_ind = 8
    elif freq==32:
        freq_ind = 9
    elif freq==64:
        freq_ind = 10
    elif freq==128:
        freq_ind = 11
    elif freq==256:
        freq_ind = 12       
    elif freq==512:
        freq_ind = 13
    elif freq=='T':
        freq_ind = 14
    else:
        print('invalid frequency specified')
        freq_ind = comp.query('SRAT?')
        
    comp.write('SRAT %d' % freq_ind)


# return 1: voltage input return 0: current input
def get_input(comp):
    inp = int(comp.query('ISRC?'))
    if inp==0 or inp==1:
        return 1
    else:
        return 0

def get_units(comp):
    inp = get_input(comp)
    sens = int(comp.query('SENS?'))
    if sens==0 or sens==1 or sens==2 or sens==3 or sens==4 or sens==5 or sens==6 or sens==7:
        if inp==1:
            return 'nV'
        else:
            return 'fA'
    elif sens==8 or sens==9 or sens==10 or sens==11 or sens==12 or sens==13 or sens==14 or sens==15 or sens==16:
        if inp==1:
            return 'uV'
        else:
            return 'pA'
    elif sens==17 or sens==18 or sens==19 or sens==20 or sens==21 or sens==22 or sens==23 or sens==24 or sens==25:
        if inp==1:
            return 'mV'
        else:
            return 'nA'
    elif sens==26:
        if inp==1:
            return 'V'
        else:
            return 'uA'
    else:
            return 'NA'


def get_scale_factor(comp):
    inp = get_input(comp)
    sens = int(comp.query('SENS?'))
    if sens==0 or sens==1 or sens==2 or sens==3 or sens==4 or sens==5 or sens==6 or sens==7:
        if inp==1:
            return 1e9
        else:
            return 1e15
    elif sens==8 or sens==9 or sens==10 or sens==11 or sens==12 or sens==13 or sens==14 or sens==15 or sens==16:
        if inp==1:
            return 1e6
        else:
            return 1e12
    elif sens==17 or sens==18 or sens==19 or sens==20 or sens==21 or sens==22 or sens==23 or sens==24 or sens==25:
        if inp==1:
            return 1e3
        else:
            return 1e9
    elif sens==26:
        if inp==1:
            return 1
        else:
            return 1e-6
    else:
            return 0
            

    


