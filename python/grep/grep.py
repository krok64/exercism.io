def grep(pattern, f_list, flags=""):
    out_line_num = False
    out_only_fnames = False
    case_insens = False
    invert_output = False
    match_all_line = False
    result = []
    for key in flags.split():
        if key=="-n":
            out_line_num = True
        elif key=="-l":
            out_only_fnames = True
        elif key=="-i":
            case_insens = True
        elif key=="-v":
            invert_output = True
        elif key=="-x":
            match_all_line = True

    if case_insens:
        pattern = pattern.lower()

    out_f_names = False
    if len(f_list) > 1:
        out_f_names = True

    for f_n in f_list:
        with open(f_n, "r") as f:
            lines = f.readlines()
        for num, line in enumerate(lines):
            match = False
            if match_all_line:
                if case_insens:
                    if pattern == line.lower()[:-1]:
                        match = True
                else:
                    if pattern == line[:-1]:
                        match = True
            else:
                if case_insens:
                    if pattern in line.lower():
                        match = True
                else:
                    if pattern in line:
                        match = True

            if out_line_num:
                line = "%d:%s" % (num + 1, line)

            if out_f_names:
                line = "%s:%s" % (f_n, line)

            if match and not invert_output:
                if out_only_fnames:
                    result.append(f_n + "\n")
                    break
                else:
                    result.append(line)
            elif not match and invert_output:
                if out_only_fnames:
                    result.append(f_n + "\n")
                    break
                else:
                    result.append(line)

    return "".join(result)
