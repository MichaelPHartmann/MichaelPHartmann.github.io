class paintElements():
    def __init__(self):
        self._include = 'templates/_include.txt'
        self.include_pages()
        self.header_include = 'templates/header_include.txt'
        self.footer_include = 'templates/footer_include.txt'
        self.head_include = 'templates/head_include.txt'

    def include_pages(self):
        with open(self._include) as f:
            include = f.readlines()
            include = map(str.strip, include)
        self.include_pages = include

    def erase_file(self, file):
        file.seek(0)
        file.truncate(0)
        return 'File Erased'

    def paint_headers(self):
        """
            Crawl directories for webpages. Possibly have a '_include.py' file to streamline this.
            Look for `<!--HEADER BEGINS HERE-->` and `<!--HEADER ENDS HERE-->` using readlines.
            Replace block with standard `header_include.txt` file.
            Save file.
        """
        with open(self.header_include, 'r') as h:
            header_lines = h.readlines()
        for file in self.include_pages:
            with open(file, 'r+') as f:
                lines = f.readlines()
                # For saefety we don't want to writing to a file that won't work properly, so we make sure that our pointers are correct.
                try:
                    begin = lines.index('<!--HEADER BEGINS HERE-->\n')
                    end = lines.index('<!--HEADER ENDS HERE-->\n')
                except:
                    print(f'Was not able to find the correct header pointers for {file}')
                    continue

                # As we pop elements, the list indexes change, so our pop index remains the same while the list changes.
                for line in range(begin, end+1):
                    remove = lines.pop(begin)

                # Just as we popped from a static index, we push the new header out from a static index, backwards.
                for h in header_lines[::-1]:
                 lines.insert(begin, h)

                # Now for the scary part, errasing and re-writing the file.
                self.erase_file(f)
                for line in lines:
                    f.write(line)




    def paint_footers(self):
        """
            Crawl directories for webpages. Possibly have a '_include.py' file to streamline this.
            Look for `<!--FOOTER BEGINS HERE-->` and `<!--FOOTER ENDS HERE-->` using readlines.
            Replace block with standard `footer_include.txt` file.
            Save file.
        """
        with open(self.footer_include, 'r') as h:
            footer_lines = h.readlines()
        for file in self.include_pages:
            with open(file, 'r+') as f:
                lines = f.readlines()
                # For saefety we don't want to writing to a file that won't work properly, so we make sure that our pointers are correct.
                try:
                    begin = lines.index('<!--FOOTER BEGINS HERE-->\n')
                except:
                    print(f'Was not able to find the correct footer begin pointers for {file}')
                    continue
                try:
                    end = lines.index('<!--FOOTER ENDS HERE-->\n')
                except:
                    print(f'Was not able to find the correct footer end pointers for {file}')
                    continue
                # As we pop elements, the list indexes change, so our pop index remains the same while the list changes.
                for line in range(begin, end+1):
                    remove = lines.pop(begin)
                # Just as we popped from a static index, we push the new footer out from a static index, backwards.
                for h in footer_lines[::-1]:
                 lines.insert(begin, h)
                # Now for the scary part, errasing and re-writing the file.
                self.erase_file(f)
                for line in lines:
                    f.write(line)

    def paint_head(self):
        """
            Crawl directories for webpages. Possibly have a '_include.py' file to streamline this.
            Look for `<!--HEAD BEGINS HERE-->` and `<!--HEAD ENDS HERE-->` using readlines.
            Replace block with standard `head_include.txt` file.
            Save file.
        """
        with open(self.head_include, 'r') as h:
            head_lines = h.readlines()
        for file in self.include_pages:
            with open(file, 'r+') as f:
                lines = f.readlines()
                # For saefety we don't want to writing to a file that won't work properly, so we make sure that our pointers are correct.
                try:
                    begin = lines.index('<!--HEAD BEGINS HERE-->\n')
                    end = lines.index('<!--HEAD ENDS HERE-->\n')
                except:
                    print(f'Was not able to find the correct head pointers for {file}')
                    continue
                # As we pop elements, the list indexes change, so our pop index remains the same while the list changes.
                for line in range(begin, end+1):
                    remove = lines.pop(begin)
                # Just as we popped from a static index, we push the new head out from a static index, backwards.
                for h in head_lines[::-1]:
                 lines.insert(begin, h)
                # Now for the scary part, errasing and re-writing the file.
                self.erase_file(f)
                for line in lines:
                    f.write(line)

if __name__ == '__main__':
    p = paintElements()
    p.paint_headers()
    p.paint_footers()
    p.paint_head()
