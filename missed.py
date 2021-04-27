from invisible_cities.types.ic_types import minmax


class S12Params:
    def __init__(self, time: minmax = minmax(1, 2), length: minmax = minmax(3, 4),
                 stride: int = 1, rebin_stride: int = 1):
        self.time = time
        self.length = length
        self.stride = stride
        self.rebin_stride = rebin_stride


def unpack_s12params(s12params):
    s1par, s2par = s12params
    return dict(
        s1_tmin=s1par.time.min,
        s1_tmax=s1par.time.max,
        s1_lmin=s1par.length.min,
        s1_lmax=s1par.length.max,

        s2_tmin=s2par.time.min,
        s2_tmax=s2par.time.max,
        s2_rebin_stride=s2par.rebin_stride,
        s2_lmin=s2par.length.min,
        s2_lmax=s2par.length.max
    )
