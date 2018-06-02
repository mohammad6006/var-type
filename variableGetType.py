import sublime
import sublime_plugin

class VariableGetTypeCommand(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if hover_zone == 1:
            for region in view.sel():
                if not region.empty():
                    s = view.substr(region)
                    if s.startswith('$'):
                        starter = region.end()
                        i = 10
                        counter = 0
                        starting = 0
                        ending = 1
                        while i:
                            nowp = starter + counter
                            if view.substr(nowp) == "=":
                                if (view.substr(nowp+1) == "'" or view.substr(nowp+1) =='"' or view.substr(nowp+2) =="'" or view.substr(nowp+2) =='"'):
                                    view.set_status('type',"Type : String")
                                elif (view.substr(nowp+1).lower() == "t" or view.substr(nowp+1).lower() =='f' or view.substr(nowp+2).lower() =="t" or view.substr(nowp+2).lower() =='f'):
                                    view.set_status('type',"Type : Boolean")
                                else:
                                    view.set_status('type',"Type : Integer")
                            counter += 1
                            i -= 1
