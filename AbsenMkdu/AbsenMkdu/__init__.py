"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import AbsenMkdu.views
import AbsenMkdu.module.mahasiswa
import AbsenMkdu.module.absen
import AbsenMkdu.module.kelas
import AbsenMkdu.module.mataKuliah