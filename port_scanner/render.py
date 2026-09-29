import json

def scan_render(output_file , dict_results):
        if output_file == None:
            for host , val in dict_results.items():
                print(f"HOST : {host}")
                print("PORT | STATE | SERVICE | LATENCY | BANNER")
                for res in val :
                    print(f"{res.port} | {res.state} | {res.service} | {res.latency} | {res.banner}")
        else:         
            _,render_format = output_file.split(".")
            if render_format not in ["csv", "json","txt"]:
                return (print(f"It's not possible to make a render with the {render_format} format "))

            with open(output_file,"w", encoding="UTF-8") as render_file:
                if render_format == "json":
                    dict_render = {}
                    for host , val in dict_results.items():
                        dict_port = {}
                        for res in val:
                            dict_port[res.port] = {"state":res.state,
                                                        "service":res.service,
                                                        "latency":res.latency,
                                                        "banner":res.banner}

                        dict_render[host] = dict_port

                    json.dump(dict_render, render_file, indent = 4)
                else:
                    render_file.write("HOST;PORT;STATE;SERVICE;LATENCY;BANNER\n")
                    for host , val in dict_results.items():
                        for res in val:
                            render_file.write(f"{host};{res.port};{res.state};{res.service};{res.latency};{res.banner}\n")