import ui

class MyTextFieldDelegate (object):

    def textfield_did_change(sender):
        v = sender.superview
        v['qte'].text = sender.text


v = ui.load_view('CasinoCalc')

v.present('sheet')
