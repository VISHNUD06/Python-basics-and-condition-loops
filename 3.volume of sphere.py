def volume_sph(f,pi,dia):
    try:
        r=dia/2
        R=r*r*r
    except:
        print('error in value')
    else:
        v=f*pi*R
        return ('volume of sphere:',v)
(f,pi,dia)=((4/3),(3.14),12)
print(volume_sph(f,pi,dia))
