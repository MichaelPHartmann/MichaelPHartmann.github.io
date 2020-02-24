with open('builder.txt', 'r') as f:
    lines = f.readlines()
    function = ''
    function_name = ''
    description = ''
    counter = 1
    for line in lines:
        line = line.rstrip()
        if '#' in line:
            line = line.strip('#')
            heading = f"""
            <mainheading>{line}</mainheading>
            <div id=thickdivline></div>
            <br>
            <br>
            """
            print(heading)
        else:    
            if '(' in line:
                function = line
                for l in line:
                    if l == '(':
                        break
                    else:
                        function_name += l
            else:
                description = line
                print(f"""
                <div class='function_list'>
                <heading id='{function_name}'>{function}<heading>
                <div id=divline></div>
                <t>{description}</t>
                <br>
                <!-- Placeholder for Future Addition -->
                <br>
                <br>
                </div>
                """)
                function_name = ''
