import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# redefining plot save parameters
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Charter"],
    "font.size": 12
})

# update savefig options for latex export
matplotlib.use("pgf")

# reading the prepared data
data = pd.read_csv('plot-data-export.csv', sep=';')
extinction_lines = [1906, 1950, 1977, 2003]

data.set_index('wellenlaenge', inplace=True)


# # Plot of calibration curve
# calib_factor = data['calibration_factor'].to_list()
# # data['calibration_factor'].plot(linestyle='.')
# plt.figure().set_figheight(2.5)
# plt.plot(data.index, calib_factor, '*', color='orange')
# # plt.plot(x, trendline, '--')
# plt.xlabel('wavelength in $\mathrm{nm}$')
# plt.ylabel('calibration factor $KF$')
# plt.grid()
# plt.ylim(bottom=0, top=1.1)
# # plt.figure().supxlabel('wavelength in $\mathrm{nm}$')
# # plt.show()
# plt.savefig('calibration-factor.pgf')
# plt.close()

# # Plot of absorption spectra
# plt.figure().set_figheight(2.5)
# data['rel-abs_dmso'].plot(label='$\mathrm{DMSO}$')
# data['rel-abs_etso4'].plot(label='$\mathrm{EtSO_4}$')
# plt.xlabel('wavelength in $\mathrm{nm}$')
# plt.ylabel('relative absorbtion rate')
# plt.ylim(bottom=0, top=1.1)
# plt.grid()
# for i in range(np.size(extinction_lines)):
#     plt.axvline(x = extinction_lines[i], color='purple', linestyle='--')
# plt.legend()
# # plt.show()
# plt.savefig('rel-absorbtion.pgf')
# plt.close()

# Plot of laser signal, absorption signal, transmission 
fig, axs = plt.subplots(2, figsize=(8,6))
axs[0].plot(data['laser-signal_dmso'], label='laser signal $\mathrm{DMSO}$')
axs[0].plot(data['abs_dmso'], label='absorption signal $\mathrm{DMSO}$')
axs[0].plot(data['trans_dmso'], label='transmission signal $\mathrm{DMSO}$')

axs[1].plot(data['laser-signal_etso4'], label='laser signal $\mathrm{EtSO_4}$')
axs[1].plot(data['abs_etso4'], label='absorption signal $\mathrm{EtSO_4}$')
axs[1].plot(data['trans_etso4'], label='transmission signal $\mathrm{EtSO_4}$')

for ax in axs.flat:
    ax.label_outer()
    for i in range(np.size(extinction_lines)):
        ax.axvline(x = extinction_lines[i], color='purple', linestyle='--')
    
fig.supylabel('intensity signal in $mV$')
fig.supxlabel('wavelength in $\mathrm{nm}$')

# plt.xlabel('wavelength in $\mathrm{nm}$')
axs[0].grid()
axs[1].grid()
axs[0].legend()
axs[1].legend()
# plt.show()
plt.savefig('laser-abs-trans.pgf')
plt.close()

# # Plot of extinction and extinction factor
# fig2, axs2 = plt.subplots(2, figsize=(6,6))
# axs2[0].plot(data['ext-fac_dmso'], label='extinction factor $\mathrm{DMSO}$')
# axs2[0].plot(data['ext-fac_etso4'], label='extinction factor $\mathrm{EtSO_4}$')

# axs2[1].plot(data['ext_dmso'], label='extinction $\mathrm{DMSO}$')
# axs2[1].plot(data['ext_etso4'], label='extinction $\mathrm{EtSO_4}$')

# for ax2 in axs2.flat:
#     ax2.label_outer()
    
# z = 0
# for ax2 in axs2.flat:
#     if z == 0:
#         ax2.set(ylabel='extinction factor in $\mathrm{cm^2} \cdot \mathrm{mol}^\mathrm{-1}$')
#         for i in range(np.size(extinction_lines)):
#             ax2.axvline(x = extinction_lines[i], color='purple', linestyle='--')
#     elif z == 1:
#         ax2.set(ylabel='relative extinction')
#         for i in range(np.size(extinction_lines)):
#             ax2.axvline(x = extinction_lines[i], color='purple', linestyle='--')
#     z = z+1

# plt.xlabel('wavelength in $\mathrm{nm}$')
# axs2[0].grid()
# axs2[1].grid()
# axs2[0].legend()
# axs2[1].legend()
# # plt.show()
# plt.savefig('extinction.pgf')
# plt.close()



# # Plot of extinction factor
# data['ext-fac_dmso'].plot(label='extinction factor $\mathrm{DMSO}$')
# data['ext-fac_etso4'].plot(label='extinction factor $\mathrm{EtSO_4}$')
# for i in range(np.size(extinction_lines)):
#     plt.axvline(x = extinction_lines[i], color='purple', linestyle='--')

# plt.xlabel('wavelength in $\mathrm{nm}$')
# plt.ylabel('extinction factor in') # ' $\frac{\mathrm{cm^2}}{\mathrm{mol}}$')
# plt.grid()
# plt.ylim(bottom=0)
# plt.legend()
# plt.show()
# # plt.savefig('ext-fac.pgf')
# # plt.close()

# # Plot of extinction
# data['ext_dmso'].plot(label='extinction $\mathrm{DMSO}$')
# data['ext_etso4'].plot(label='extinction $\mathrm{EtSO_4}$')
# for i in range(np.size(extinction_lines)):
#     plt.axvline(x = extinction_lines[i], color='purple', linestyle='--')
    
# plt.xlabel('wavelength in $\mathrm{nm}$')
# plt.ylabel('relative extinction')
# plt.grid()
# plt.ylim(bottom=0, top=2.3)
# plt.legend()
# plt.show()
# # plt.savefig('extinction.pgf')
# # plt.close()