# coding: utf-8

import os
import sys
import time
from my_modules.screen_manager import HatenaManager, QiitaManager, NoteManager

hatena_manager = HatenaManager()
hatena_manager.browse("https://xxx.hatenablog.com", "hatena", "entry");

qiita_manager = QiitaManager()
qiita_manager.browse("https://qiita.com/xxx", "qiita", "items")

note_manager = NoteManager()
note_manager.browse("https://note.com/xxx", "note", "xxx/n")