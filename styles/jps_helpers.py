
# Helper to choose Physical Society-style figure sizes (inches).
# Single column ≈ 85 mm, 1.5 column ≈ 114 mm, double column ≈ 174 mm.
def jps_size(width='single', aspect=0.62):
    widths_mm = {'single': 85, 'onehalf': 114, 'double': 174}
    w_mm = widths_mm.get(width, 85)
    w_in = w_mm / 25.4
    h_in = w_in * aspect
    return (w_in, h_in)
