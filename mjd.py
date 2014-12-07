from astropy.io import fits

file = fits.open('Image189.fits'); MJD = file[0].header['JD'] - 2400000.5; print MJD
