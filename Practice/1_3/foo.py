try:
    raise RuntimeError('What a kerfuffle')
except RuntimeError as e:
    print('Failed : Reason', e)
