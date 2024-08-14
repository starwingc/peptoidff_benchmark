import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 17, 3, 42480])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDG1tQ0lGSGVhZGVyc3EIXXEJTmFVDGFyb21hdGljTW9kZXEKSwFLAX2HVQp2ZHdEZW5zaXR5cQtLAUdAFAAAAAAAAH2HVQZoaWRkZW5xDEsBiX2HVQ1hcm9tYXRpY0NvbG9ycQ1LAU59h1UPcmliYm9uU21vb3RoaW5ncQ5LAUsAfYdVCWF1dG9jaGFpbnEPSwGIfYdVCnBkYlZlcnNpb25xEEsBSwB9h1UIb3B0aW9uYWxxEX1xElUIb3BlbmVkQXNxE4iJSwEoVSdzbWlsZXM6Q0MoPU8pTihbQ0BASF0oQyljMWNjY2MyY2NjY2MyMSlOVQNQREJxFEsBdHEVfYeHc1UPbG93ZXJDYXNlQ2hhaW5zcRZLAYl9h1UJbGluZVdpZHRocRdLAUc/8AAAAAAAAH2HVQ9yZXNpZHVlTGFiZWxQb3NxGEsBSwB9h1UEbmFtZXEZSwFYGAAAAHNtaWxlczpDQyg9TylOKFtDQEBIXS4uLn2HVQ9hcm9tYXRpY0Rpc3BsYXlxGksBiX2HVQ9yaWJib25TdGlmZm5lc3NxG0sBRz/pmZmZmZmafYdVCnBkYkhlYWRlcnNxHF1xHX1xHmFVA2lkc3EfSwFLAEsAhn2HVQ5zdXJmYWNlT3BhY2l0eXEgSwFHv/AAAAAAAAB9h1UQYXJvbWF0aWNMaW5lVHlwZXEhSwFLAn2HVRRyaWJib25IaWRlc01haW5jaGFpbnEiSwGIfYdVB2Rpc3BsYXlxI0sBiH2HdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksBVQEgfYdVC2ZpbGxEaXNwbGF5cQNLAYl9h1UEbmFtZXEESwFYAwAAAFVOS32HVQVjaGFpbnEFSwFYAQAAACB9h1UOcmliYm9uRHJhd01vZGVxBksBSwJ9h1UCc3NxB0sBiYmGfYdVCG1vbGVjdWxlcQhLAUsAfYdVC3JpYmJvbkNvbG9ycQlLAU59h1UFbGFiZWxxCksBWAAAAAB9h1UKbGFiZWxDb2xvcnELSwFOfYdVCGZpbGxNb2RlcQxLAUsBfYdVBWlzSGV0cQ1LAYl9h1ULbGFiZWxPZmZzZXRxDksBTn2HVQhwb3NpdGlvbnEPXXEQSwFLAYZxEWFVDXJpYmJvbkRpc3BsYXlxEksBiX2HVQhvcHRpb25hbHETfVUEc3NJZHEUSwFK/////32HdS4='))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLH0sBfYdVCHZkd0NvbG9ycQNLH059h1UEbmFtZXEESx9YAwAAAEMxM31xBShYAwAAAEMxMl1xBksOYVgDAAAAQzExXXEHSw1hWAMAAABDMTBdcQhLDGFYAgAAAE8xXXEJSwJhWAMAAABDMTRdcQpLEGFYAgAAAEM5XXELSwthWAIAAABDOF1xDEsKYVgCAAAAQzNdcQ1LBGFYAgAAAEMyXXEOSwFhWAIAAABDMV1xD0sAYVgCAAAAQzddcRBLCWFYAgAAAEM2XXERSwhhWAIAAABDNV1xEksHYVgCAAAAQzRdcRNLBmFYAwAAAEgxMF1xFEsZYVgDAAAASDExXXEVSxphWAMAAABIMTJdcRZLG2FYAwAAAEgxM11xF0scYVgDAAAASDE0XXEYSx1hWAMAAABIMTVdcRlLHmFYAgAAAE4xXXEaSwNhWAIAAABIOF1xG0sXYVgCAAAASDldcRxLGGFYAgAAAEgyXXEdSxFhWAIAAABIM11xHksSYVgCAAAASDFdcR9LBWFYAgAAAEg2XXEgSxVhWAIAAABIN11xIUsWYVgCAAAASDRdcSJLE2FYAgAAAEg1XXEjSxRhdYdVA3Zkd3EkSx+JfYdVDnN1cmZhY2VEaXNwbGF5cSVLH4l9h1UFY29sb3JxJksfSwN9cScoSwFdcShLAmFOXXEpKEsASwFLBEsGSwdLCEsJSwpLC0sMSw1LDksPSxBlSwJdcSpLA2F1h1UJaWRhdG1UeXBlcStLH4l9h1UGYWx0TG9jcSxLH1UAfYdVBWxhYmVscS1LH1gAAAAAfYdVDnN1cmZhY2VPcGFjaXR5cS5LH0e/8AAAAAAAAH2HVQdlbGVtZW50cS9LH0sBfXEwKEsIXXExSwJhSwZdcTIoSwBLAUsESwZLB0sISwlLCksLSwxLDUsOSw9LEGVLB11xM0sDYXWHVQpsYWJlbENvbG9ycTRLH059h1UMc3VyZmFjZUNvbG9ycTVLH059h1UPc3VyZmFjZUNhdGVnb3J5cTZLH1gEAAAAbWFpbn2HVQZyYWRpdXNxN0sfRz/wAAAAAAAAfXE4KEc/+zMzQAAAAF1xOShLAEsBSwRLBksHSwhLCUsKSwtLDEsNSw5LD0sQZUc/964UgAAAAF1xOksCYUc/+gAAAAAAAF1xO0sDYXWHVQpjb29yZEluZGV4cTxdcT1LAEsfhnE+YVULbGFiZWxPZmZzZXRxP0sfTn2HVRJtaW5pbXVtTGFiZWxSYWRpdXNxQEsfRwAAAAAAAAAAfYdVCGRyYXdNb2RlcUFLH0sCfYdVCG9wdGlvbmFscUJ9cUMoVQxzZXJpYWxOdW1iZXJxRIiIXXFFSwFLH4ZxRmGHVQdiZmFjdG9ycUeIiUsfRwAAAAAAAAAAfYeHVQlvY2N1cGFuY3lxSIiJSx9HP/AAAAAAAAB9h4d1VQdkaXNwbGF5cUlLH4h9h3Uu'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECSyBOfYdVBWF0b21zcQNdcQQoXXEFKEsCSwNlXXEGKEsDSwRlXXEHKEsDSwVlXXEIKEsFSwZlXXEJKEsGSwdlXXEKKEsGSwhlXXELKEsGSwllXXEMKEsJSwplXXENKEsKSwtlXXEOKEsLSwxlXXEPKEsMSw1lXXEQKEsNSw5lXXERKEsOSw9lXXESKEsPSxBlXXETKEsQSxFlXXEUKEsRSxJlXXEVKEsNSxJlXXEWKEsJSxJlXXEXKEsCSxNlXXEYKEsCSxRlXXEZKEsCSxVlXXEaKEsFSxZlXXEbKEsISxdlXXEcKEsISxhlXXEdKEsISxllXXEeKEsKSxplXXEfKEsLSxtlXXEgKEsMSxxlXXEhKEsOSx1lXXEiKEsPSx5lXXEjKEsQSx9lXXEkKEsRSyBlZVUFbGFiZWxxJUsgWAAAAAB9h1UIaGFsZmJvbmRxJksgiH2HVQZyYWRpdXNxJ0sgRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cShLIE59h1UIZHJhd01vZGVxKUsgSwF9h1UIb3B0aW9uYWxxKn1VB2Rpc3BsYXlxK0sgSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQFLAH1xAihLAF1xAyhHQBGye7L+xW1Hv9xGc4HX2/VHP+uGwiaAnUmHcQRHQAhzgdfb9IhHP8VWbPQfIS1HP+YGjbi6xxGHcQVHQAOHKwIMSbpHP+HigkC3gDRHP/qDEm6XjVCHcQZHQAQiaAnUlRhHP9GX9itq59VHv+FYEGJN0vKHcQdHP/L987ZFoctHP+u5jH4oJAtHv+axxDLKV6iHcQhHP/Dk92X9ittHP/rMzMzMzM1HP4R64UeuFHuHcQlHP/DLKV6eGwlHP/a2rn1WbPRHwAEIMSbpeNWHcQpHP8FUyYXwb2lHv8gJ1JUYKplHv96D5CWu5jKHcQtHP9wiaAnUlRhHv/gTqSowVTJHv+Rs9B8hLXeHcQxHv+Ce7L+xW1dHwAPysCDEm6ZHv9tkWhysCDGHcQ1Hv/ycDr7fpEBHwAFe0ojOcDtHv6v0h/y5I6OHcQ5HwAEdSVGCqZNHv+pRGc4HX3BHP79PDYRNATuHcQ9HwAuDRtxdY4hHv9zbi6xxDLNHP+A24uscQy2HcRBHwA3xqfvnbItHP+u0ojOcDr9HP+Vh5Pdl/YuHcRFHwAZFbVz6rNpHP/2tq59Vmz1HP91JUYKpkwyHcRJHv/g/FBIFvAJHP/iGWUr08NhHP7WOIZZSvTyHcRNHv/KZML4N7SlHP8dzGPxQSBdHv7Y4hllK9PGHcRRHQBLDLKV6eGxHv9xvaURnOB1HP/6scQyyleqHcRVHQBGqfvnbItFHv/dxdY4hllNHP98L4N7SiM6HcRZHQBSe7L+xW1dHP8JrULDye7NHP9Nfb9If8uWHcRdHQAgSOinHeadHv6Pdl/YrauhHv/URnOB19v2HcRhHP/LjvNNahYhHP+ONT987ZFpHwAbJHRTjvNOHcRlHP67SiM5wOvtHP/3BVMmF8G9HwAIG9pRGc4KHcRpHP/z2lEZzgdhHQAF08NhE0BRHwAJgdfb9If+HcRtHP/cGJN0vGqBHv/yZmZmZmZpHv+3k92X9ituHcRxHv9AiaAnUlRhHwAw/sVtXPqtHv+IJ1JUYKpmHcR1HwAQrNnoPkJdHwAeWUr08NhFHP7rAgxJul42HcR5HwBDFh5Pdl/ZHv/NNATqSowVHP+WHk92X9iuHcR9HwBL4bCJoCdVHP/JgqmTC+DhHP+7Vz6rNnoSHcSBHwAhpRGc4HX5HQAcj1wo9cKRHP+L0HyEtdzKHcSFHv+kNhE0BOpNHQAJ64UeuFHtHv7N7SiM5wOyHcSJlVQZhY3RpdmVxI0sAdXMu'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'gold': ((1, 0.843137, 0), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'),
u'Pr': ((0.85098, 1, 0.780392), 1, u'default'), u'deep pink': ((1, 0.0784314, 0.576471), 1, u'default'), u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'purple': ((0.627451, 0.12549, 0.941176), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'),
u'Mt': ((0.921569, 0, 0.14902), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'), u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), u'sky blue': ((0.529412, 0.807843, 0.921569), 1, u'default'), u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'plum': ((0.866667, 0.627451, 0.866667), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'dodger blue': ((0.117647, 0.564706, 1), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'),
u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'light green': ((0.564706, 0.933333, 0.564706), 1, u'default'),
u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'), u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'), u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'salmon': ((0.980392, 0.501961, 0.447059), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'),
u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), u'light gray': ((0.827451, 0.827451, 0.827451), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 4, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (6, (u'H', (1, 1, 1, 1)), {(u'green', (0, 1, 0, 1)): [5], (u'N', (0.188235, 0.313725, 0.972549, 1)): [2], (u'O', (1, 0.0509804, 0.0509804, 1)): [1], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'yellow', (1, 1, 0, 1)): [4]})
	viewerInfo = {'cameraAttrs': {'center': (0.2063, -0.3193, -0.35559999046326), 'fieldOfView': 54.3714685806, 'nearFar': (6.0355896087386, -6.7467895896651), 'ortho': False, 'eyeSeparation': 50.8, 'focal': -0.35559999046326}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 10.567702617801, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 5, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': None}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [ ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


try:
	from BuildStructure.gui import _sessionRestore
	_sessionRestore({'mapped': 1})
except:
	reportRestoreError("Failure restoring Build Structure")


def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1920, 955)
	xformMap = {0: (((0, 0, 1), 0), (0, 0, 0), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 65: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

