# Key Findings from PYC Analysis

## Core Application Modules

- `utils`
- `util`
- `install`
- `install_ui`
- `shutil`

## Key Classes

### Module: translate

- `Translate`

### Module: dis

- `Instruction (_Instruction)`
- `Bytecode`

### Module: .py

- `AddrlistClass`
- `AddressList (AddrlistClass)`

### Module: install

- `Style`
- `UI`

### Module: parser

- `Parser`
- `HeaderParser (Parser)`
- `BytesParser`
- `BytesHeaderParser (BytesParser)`

### Module: feedparser

- `BufferedSubFile (object)`
- `FeedParser`
- `BytesFeedParser (FeedParser)`

### Module: lzma

- `LZMAFile (_compression.BaseStream)`

### Module: csv

- `Dialect`
- `excel (Dialect)`
- `excel_tab (excel)`
- `unix_dialect (Dialect)`
- `DictReader`
- `DictWriter`

### Module: numbers

- `Complex (Number)`
- `Real (Complex)`
- `Rational (Real)`
- `Integral (Rational)`

### Module: _compression

- `BaseStream (io.BufferedIOBase)`
- `DecompressReader (io.RawIOBase)`

### Module: copy

- `Error (Exception)`

### Module: fractions

- `Fraction (numbers.Rational)`
  - Methods: `__add__`, `__radd__`, `forward`, `reverse`

### Module: typing

- `Starship`
- `Connection`
- `FastConnector (Connection)`

### Module: webbrowser

- `BaseBrowser (object)`
  - Methods: `__init__`, `__init__`
- `GenericBrowser (BaseBrowser)`
  - Methods: `__init__`, `__init__`
- `BackgroundBrowser (GenericBrowser)`
  - Methods: `__init__`, `__init__`
- `UnixBrowser (BaseBrowser)`
  - Methods: `__init__`, `__init__`
- `Mozilla (UnixBrowser)`
  - Methods: `__init__`, `__init__`
- `Netscape (UnixBrowser)`
  - Methods: `__init__`, `__init__`
- `Galeon (UnixBrowser)`
  - Methods: `__init__`, `__init__`
- `Chrome (UnixBrowser)`
  - Methods: `__init__`, `__init__`
- `Opera (UnixBrowser)`
  - Methods: `__init__`, `__init__`
- `Elinks (UnixBrowser)`
  - Methods: `__init__`, `__init__`
- `Konqueror (BaseBrowser)`
  - Methods: `__init__`, `__init__`
- `Grail (BaseBrowser)`
  - Methods: `__init__`, `__init__`
- `WindowsDefault (BaseBrowser)`
- `MacOSX (BaseBrowser)`
- `MacOSXOSAScript (BaseBrowser)`

### Module: textwrap

- `TextWrapper`
  - Methods: `predicate`

### Module: pprint

- `PrettyPrinter`

### Module: ipaddress

- `AddressValueError (ValueError)`
- `NetmaskValueError (ValueError)`

### Module: statistics

- `StatisticsError (ValueError)`

### Module: _strptime

- `LocaleTime (object)`
- `TimeRE (dict)`

### Module: calendar

- `IllegalMonthError (ValueError)`
- `IllegalWeekdayError (ValueError)`
- `Calendar (object)`
- `TextCalendar (Calendar)`
- `HTMLCalendar (Calendar)`
- `different_locale`
- `LocaleTextCalendar (TextCalendar)`
- `LocaleHTMLCalendar (HTMLCalendar)`

### Module: shlex

- `shlex`

### Module: gzip

- `BadGzipFile (OSError)`
- `GzipFile (_compression.BaseStream)`

### Module: _threading_local

- `local`

### Module: pathlib

- `PurePath (object)`
  - Methods: `check_eloop`
- `PurePosixPath (PurePath)`
  - Methods: `check_eloop`
- `PureWindowsPath (PurePath)`
  - Methods: `check_eloop`
- `Path (PurePath)`
  - Methods: `check_eloop`

### Module: _py_abc

- `ABCMeta (type)`

### Module: contextlib

- `AbstractContextManager (abc.ABC)`
  - Methods: `inner`, `some_generator`, `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `AbstractAsyncContextManager (abc.ABC)`
  - Methods: `inner`, `some_generator`, `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `ContextDecorator (object)`
  - Methods: `inner`, `some_generator`, `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `AsyncContextDecorator (object)`
  - Methods: `some_generator`, `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `closing (AbstractContextManager)`
  - Methods: `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `aclosing (AbstractAsyncContextManager)`
  - Methods: `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `redirect_stdout (_RedirectStream)`
  - Methods: `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `redirect_stderr (_RedirectStream)`
  - Methods: `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `suppress (AbstractContextManager)`
  - Methods: `_exit_wrapper`, `_fix_exception_context`, `_fix_exception_context`
- `ExitStack (AbstractContextManager, _BaseExitStack)`
  - Methods: `_fix_exception_context`, `_fix_exception_context`
- `AsyncExitStack (AbstractAsyncContextManager, _BaseExitStack)`
  - Methods: `_fix_exception_context`
- `nullcontext (AbstractAsyncContextManager, AbstractContextManager)`

### Module: py_compile

- `PyCompileError (Exception)`
- `PycInvalidationMode (enum.Enum)`

### Module: string

- `Template`
  - Methods: `convert`, `convert`
- `Formatter`

### Module: dataclasses

- `FrozenInstanceError (AttributeError)`
- `InitVar`
- `Field`

### Module: bz2

- `BZ2File (_compression.BaseStream)`

### Module: tracemalloc

- `Statistic`
- `StatisticDiff`
- `Trace`
- `BaseFilter`
- `Filter (BaseFilter)`
- `DomainFilter (BaseFilter)`
- `Snapshot`

### Module: parse

- `DefragResult (_ResultMixinStr, _DefragResultBase)`
- `SplitResult (_NetlocResultMixinStr, _SplitResultBase)`
- `ParseResult (_NetlocResultMixinStr, _ParseResultBase)`
- `DefragResultBytes (_ResultMixinBytes, _DefragResultBase)`
- `SplitResultBytes (_NetlocResultMixinBytes, _SplitResultBase)`
- `ParseResultBytes (_NetlocResultMixinBytes, _ParseResultBase)`
- `Quoter (collections.defaultdict)`

### Module: ttk

- `Widget (tkinter.Widget)`
  - Methods: `adjust_label`
- `Button (Widget)`
  - Methods: `adjust_label`
- `Checkbutton (Widget)`
  - Methods: `adjust_label`
- `Entry (tkinter.Entry, Widget)`
  - Methods: `adjust_label`
- `Combobox (Entry)`
  - Methods: `adjust_label`
- `Frame (Widget)`
  - Methods: `adjust_label`
- `Label (Widget)`
  - Methods: `adjust_label`
- `Labelframe (Widget)`
  - Methods: `adjust_label`
- `Menubutton (Widget)`
  - Methods: `adjust_label`
- `Notebook (Widget)`
  - Methods: `adjust_label`
- `Panedwindow (tkinter.PanedWindow, Widget)`
  - Methods: `adjust_label`
- `Progressbar (Widget)`
  - Methods: `adjust_label`
- `Radiobutton (Widget)`
  - Methods: `adjust_label`
- `Scale (tkinter.Scale, Widget)`
  - Methods: `adjust_label`
- `Scrollbar (tkinter.Scrollbar, Widget)`
  - Methods: `adjust_label`
- `Separator (Widget)`
  - Methods: `adjust_label`
- `Sizegrip (Widget)`
  - Methods: `adjust_label`
- `Spinbox (Entry)`
  - Methods: `adjust_label`
- `Treeview (tkinter.YView, tkinter.XView, Widget)`
  - Methods: `adjust_label`
- `LabeledScale (Frame)`
  - Methods: `adjust_label`
- `OptionMenu (Menubutton)`

### Module: readers

- `FileReader (abc.TraversableResources)`
- `ZipReader (abc.TraversableResources)`
- `MultiplexedPath (abc.Traversable)`
- `NamespaceReader (abc.TraversableResources)`

### Module: _bootstrap

- `ModuleSpec`
- `BuiltinImporter`
- `FrozenImporter`

### Module: _text

- `FoldedCase (str)`

### Module: _meta

- `PackageMetadata (Protocol)`
- `SimplePath (Protocol)`

### Module: _collections

- `FreezableDefaultDict (collections.defaultdict)`

### Module: _adapters

- `Message (email.message.Message)`
  - Methods: `redent`, `transform`

### Module: contentmanager

- `ContentManager`

### Module: _header_value_parser

- `TokenList (list)`
- `WhiteSpaceTokenList (TokenList)`
- `UnstructuredTokenList (TokenList)`
- `Phrase (TokenList)`
- `Word (TokenList)`
- `CFWSList (WhiteSpaceTokenList)`
- `Atom (TokenList)`
- `Token (TokenList)`
- `EncodedWord (TokenList)`
- `QuotedString (TokenList)`
- `BareQuotedString (QuotedString)`
- `Comment (WhiteSpaceTokenList)`
- `Address (TokenList)`
- `MailboxList (TokenList)`
- `GroupList (TokenList)`
- `Group (TokenList)`
- `NameAddr (TokenList)`
- `AngleAddr (TokenList)`
- `ObsRoute (TokenList)`
- `Mailbox (TokenList)`
- `InvalidMailbox (TokenList)`
- `Domain (TokenList)`
- `DotAtom (TokenList)`
- `DotAtomText (TokenList)`
- `NoFoldLiteral (TokenList)`
- `AddrSpec (TokenList)`
- `ObsLocalPart (TokenList)`
- `DisplayName (Phrase)`
- `LocalPart (TokenList)`
- `DomainLiteral (TokenList)`
- `MIMEVersion (TokenList)`
- `Parameter (TokenList)`
- `InvalidParameter (Parameter)`
- `Attribute (TokenList)`
- `Section (TokenList)`
- `Value (TokenList)`
- `MimeParameters (TokenList)`
- `ParameterizedHeaderValue (TokenList)`
- `ContentType (ParameterizedHeaderValue)`
- `ContentDisposition (ParameterizedHeaderValue)`
- `ContentTransferEncoding (TokenList)`
- `HeaderLabel (TokenList)`
- `MsgID (TokenList)`
- `MessageID (MsgID)`
- `InvalidMessageID (MessageID)`
- `Header (TokenList)`
- `Terminal (str)`
- `WhiteSpaceTerminal (Terminal)`
- `ValueTerminal (Terminal)`
- `EWWhiteSpaceTerminal (WhiteSpaceTerminal)`

### Module: headerregistry

- `BaseHeader (str)`
- `UnstructuredHeader`
- `UniqueUnstructuredHeader (UnstructuredHeader)`
- `DateHeader`
- `UniqueDateHeader (DateHeader)`
- `AddressHeader`
- `UniqueAddressHeader (AddressHeader)`
- `SingleAddressHeader (AddressHeader)`
- `UniqueSingleAddressHeader (SingleAddressHeader)`
- `MIMEVersionHeader`
- `ParameterizedMIMEHeader`

### Module: generator

- `Generator`
- `BytesGenerator (Generator)`
- `DecodedGenerator (Generator)`

### Module: errors

- `MessageError (Exception)`
- `MessageParseError (MessageError)`
- `HeaderParseError (MessageParseError)`
- `BoundaryError (MessageParseError)`
- `MultipartConversionError (TypeError, MessageError)`
- `CharsetError (MessageError)`
- `HeaderWriteError (MessageError)`
- `MessageDefect (ValueError)`
- `NoBoundaryInMultipartDefect (MessageDefect)`
- `StartBoundaryNotFoundDefect (MessageDefect)`
- `CloseBoundaryNotFoundDefect (MessageDefect)`
- `FirstHeaderLineIsContinuationDefect (MessageDefect)`
- `MisplacedEnvelopeHeaderDefect (MessageDefect)`
- `MissingHeaderBodySeparatorDefect (MessageDefect)`
- `MultipartInvariantViolationDefect (MessageDefect)`
- `InvalidMultipartContentTransferEncodingDefect (MessageDefect)`
- `UndecodableBytesDefect (MessageDefect)`
- `InvalidBase64PaddingDefect (MessageDefect)`
- `InvalidBase64CharactersDefect (MessageDefect)`
- `InvalidBase64LengthDefect (MessageDefect)`
- `HeaderDefect (MessageDefect)`
- `InvalidHeaderDefect (HeaderDefect)`
- `HeaderMissingRequiredValue (HeaderDefect)`
- `NonPrintableDefect (HeaderDefect)`
- `ObsoleteHeaderDefect (HeaderDefect)`
- `NonASCIILocalPartDefect (HeaderDefect)`
- `InvalidDateDefect (HeaderDefect)`

### Module: vdict

- `VDFDict (dict)`

## Notable Function Patterns

### File Operations

- **signal**: `pthread_sigmask`
- **install**: `_on_open_link`
- **feedparser**: `close`, `readline`, `unreadline`, `close`
- **lzma**: `close`, `closed`, `readable`, `write`
- **csv**: `writeheader`, `writerow`, `writerows`
- **_compression**: `_check_not_closed`, `_check_can_read`, `_check_can_write`, `readable`, `close`, `readinto`, `readall`
- **typing**: `_remove_dups_flatten`
- **webbrowser**: `open_new`, `open_new_tab`, `open_new`, `open_new_tab`
- **pprint**: `isreadable`, `isreadable`
- **shlex**: `read_token`
- **gzip**: `write32u`, `read`, `_init_write`, `_write_gzip_header`, `write`, `closed`, `close`, `readable`, `_init_read`, `_read_exact`, `_read_gzip_header`, `_add_read_data`, `_read_eof`
- **_threading_local**: `thread_deleted`
- **pathlib**: `readlink`, `read_bytes`, `write_bytes`, `readlink`, `chmod`, `lchmod`, `rmdir`, `rename`
- **contextlib**: `close`
- **bz2**: `close`, `closed`, `readable`, `readinto`, `write`, `writelines`
- **selectors**: `close`
- **ttk**: `selection_remove`
- **readers**: `remove_duplicates`, `open_resource`, `read_bytes`, `read_text`, `open`
- **_bootstrap**: `_call_with_frames_removed`
- **_meta**: `read_text`
- **generator**: `write`, `_write_lines`, `_write`, `_write_headers`, `write`, `_write_headers`
- **vdict**: `remove_all_for`

### System Operations

- **feedparser**: `_call_parse`
- **typing**: `__call__`
- **contextlib**: `__call__`, `__call__`, `callback`, `push_async_callback`
- **_bootstrap**: `_call_with_frames_removed`

### Network Operations

- **install**: `_on_accept`

### Gui Operations

- **dis**: `findlabels`
- **inspect**: `isframe`
- **tracemalloc**: `_match_frame_impl`, `_match_frame`
- **ttk**: `adjust_label`
- **_bootstrap**: `_call_with_frames_removed`

### Crypto Operations

- **signal**: `signal`, `getsignal`, `valid_signals`
- **fractions**: `__hash__`
- **pathlib**: `__hash__`
- **dataclasses**: `_field_assign`, `_hash_fn`, `_hash_set_none`, `_hash_add`, `_hash_exception`
- **tracemalloc**: `__hash__`, `__hash__`, `__hash__`
- **_text**: `__hash__`
- **generator**: `_handle_multipart_signed`
- **vdict**: `_verify_key_tuple`

### Data Processing

- **.py**: `parsedate_tz`, `_parsedate_tz`, `parsedate`
- **feedparser**: `_call_parse`, `_parsegen`, `_parse_headers`
- **pathlib**: `parse_parts`, `join_parsed_parts`, `_parse_args`, `_from_parsed_parts`, `_format_parsed_parts`
- **string**: `parse`
- **tracemalloc**: `dump`, `load`
- **parse**: `urlunparse`
- **ttk**: `_load_tile`
- **_abc**: `load_module`
- **_bootstrap**: `_load_module_shim`, `spec_from_loader`, `_load_backward_compatible`, `_load_unlocked`, `_load`, `load_module`, `_find_and_load_unlocked`, `_find_and_load`
- **_meta**: `json`
- **_collections**: `parse`
- **_adapters**: `json`
- **headerregistry**: `parse`, `parse`, `value_parser`, `parse`, `parse`, `parse`
- **_policybase**: `header_source_parse`, `header_store_parse`, `header_fetch_parse`
- **_parseaddr**: `parsedate_tz`, `_parsedate_tz`, `parsedate`

## Import Dependencies

### Gui Libraries

- **install**: `tk`, `ttk`
- **ttk**: `tkinter`, `_splitdict`

### Network Libraries

- **socket**: `_socket`, `*`
- **utils**: `socket`, `urllib`
- **webbrowser**: `socket`
- **pathlib**: `urlquote_from_bytes`
- **_header_value_parser**: `urllib`

### System Libraries

- **zipfile**: `os`, `posixpath`, `shutil`, `stat`, `sys`
- **shutil**: `os`, `sys`, `stat`
- **tempfile**: `_os`
- **translate**: `os`, `sys`
- **dis**: `sys`
- **fnmatch**: `os`, `posixpath`
- **random**: `_sin`, `_urandom`, `_os`
- **threading**: `_os`, `_sys`
- **platform**: `os`, `sys`, `subprocess`, `subprocess`
- **glob**: `os`, `stat`, `sys`
- **install**: `os`, `sys`
- **tarfile**: `sys`, `os`, `shutil`, `stat`
- **socket**: `os`, `sys`
- **datetime**: `sys`
- **tokenize**: `sys`
- **policy**: `sys`
- **utils**: `os`
- **iterators**: `sys`
- **lzma**: `os`
- **argparse**: `_os`, `_sys`
- **_compression**: `sys`
- **fractions**: `sys`
- **inspect**: `os`, `sys`
- **typing**: `sys`
- **webbrowser**: `os`, `shutil`, `sys`, `subprocess`
- **pprint**: `_sys`
- **base64**: `sys`
- **getopt**: `os`
- **calendar**: `sys`
- **subprocess**: `os`, `sys`
- **shlex**: `os`, `sys`
- **pickle**: `sys`, `maxsize`
- **gzip**: `sys`, `os`
- **pathlib**: `os`, `posixpath`, `sys`, `S_ISFIFO`
- **contextlib**: `sys`
- **uu**: `os`, `sys`
- **py_compile**: `os`, `os`, `sys`
- **dataclasses**: `sys`
- **gettext**: `os`, `sys`
- **optparse**: `sys`, `os`
- **bz2**: `os`
- **_pydecimal**: `sys`
- **tracemalloc**: `os`
- **selectors**: `sys`
- **parse**: `sys`
- **ttk**: `os`
- **_bootstrap_external**: `sys`, `_os`, `_os`
- **_header_value_parser**: `sys`
- **generator**: `sys`
- **vdict**: `sys`

### Data Libraries

- **translate**: `json`
- **decoder**: `scanner`
- **csv**: `__doc__`, `_Dialect`
- **pickle**: `_compat_pickle`
- **tracemalloc**: `pickle`
- **_bootstrap_external**: `marshal`

### Crypto Libraries

- **utils**: `_AddressList`

### Compression Libraries

- **lzma**: `*`, `_decode_filter_properties`
- **bz2**: `BZ2Decompressor`
- **readers**: `zipfile`

### Misc Libraries

- **zipfile**: `time`
- **translate**: `logging`
- **dis**: `argparse`
- **.py**: `time`, `calendar`
- **random**: `_urandom`, `_random`
- **threading**: `_time`
- **install**: `time`
- **tarfile**: `time`
- **datetime**: `_time`
- **utils**: `time`, `random`, `datetime`, `mktime_tz`
- **pprint**: `time`
- **statistics**: `random`
- **_strptime**: `time`, `calendar`, `datetime_timezone`
- **calendar**: `datetime`, `argparse`
- **subprocess**: `time`, `_time`
- **gzip**: `time`, `argparse`
- **py_compile**: `argparse`
- **_parseaddr**: `time`, `calendar`
- **generator**: `time`, `random`

## Interesting Strings

### random_pycdas.dis

- `
                        196     CALL_FUNCTION                   1
                        198     R...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
        314     LOAD_NAME                       60: Random
        316     CALL_FUNCTION           ...`
- `,)
        502     CALL_FUNCTION_KW                1
        504     POP_TOP                        ...`
- `
                        46      LOAD_GLOBAL                     4: DeprecationWarning
             ...`
- `
                266     MAKE_FUNCTION                   0
                268     STORE_NAME       ...`
- `
                        284     LOAD_GLOBAL                     4: DeprecationWarning
             ...`
- `
                44      MAKE_FUNCTION                   8
                46      LOAD_GLOBAL      ...`
- `
                        20      CALL_FUNCTION                   1
                        22      R...`
- `
                        264     LOAD_GLOBAL                     4: DeprecationWarning
             ...`
- `
                        174     MAKE_FUNCTION                   8
                        176     L...`
- `
                22      MAKE_FUNCTION                   1
                24      STORE_NAME       ...`
- `
                136     LOAD_FAST                       9: xbar
                138     LOAD_FAST  ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        296     LOAD_NAME                       48: _random
        298     LOAD_ATTR              ...`
- `
                        12      CALL_FUNCTION                   1
                        14      R...`
- `
                250     MAKE_FUNCTION                   0
                252     STORE_NAME       ...`
- `
                        12      CALL_METHOD                     2
                        14      L...`
- `
                        188     CALL_FUNCTION                   1
                        190     R...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- Plus 43 more strings...

### inspect_pycdas.dis

- `
                        16      COMPARE_OP                      2 (==)
                        18  ...`
- `)
                        26      BUILD_CONST_KEY_MAP             2
                        28      ...`
- `
                54      CALL_FUNCTION                   2
                56      POP_JUMP_IF_FALSE...`
- `
                        30      CALL_FUNCTION                   1
                        32      R...`
- `)
                        10      BUILD_CONST_KEY_MAP             2
                        12      ...`
- `
                80      COMPARE_OP                      2 (==)
                82      POP_JUMP_IF_...`
- `
        444     MAKE_FUNCTION                   0
        446     STORE_NAME                      5...`
- `
                12      MAKE_FUNCTION                   1
                14      STORE_FAST       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                222     MAKE_FUNCTION                   8
                224     LOAD_CONST       ...`
- `
                350     CALL_FUNCTION                   2
                352     POP_JUMP_IF_FALSE...`
- `,)
                22      CALL_FUNCTION_KW                3
                24      POP_TOP        ...`
- `
                        128     LOAD_FAST                       2: formatted
                      ...`
- `
                50      LOAD_GLOBAL                     3: _void
                52      CALL_FUNCT...`
- `
                270     BINARY_SUBSCR                   
                272     STORE_FAST        ...`
- `
                348     CALL_FUNCTION                   2
                350     POP_JUMP_IF_FALSE...`
- `
        992     MAKE_FUNCTION                   0
        994     STORE_NAME                      1...`
- `
        1088    STORE_NAME                      125: GEN_CLOSED
        1090    LOAD_CONST         ...`
- `
                504     LOAD_CONST                      2: None
                506     CALL_FUNCTI...`
- `
                112     MAKE_FUNCTION                   0
                114     CALL_FUNCTION    ...`
- Plus 290 more strings...

### _pydecimal_pycdas.dis

- `,)
                        8       CALL_FUNCTION_KW                2
                        10     ...`
- `
        988     MAKE_FUNCTION                   1
        990     STORE_NAME                      1...`
- `,)
                        28      CALL_FUNCTION_KW                1
                        30     ...`
- `
                226     BINARY_SUBSCR                   
                228     LOAD_CONST        ...`
- `
                        994     LOAD_FAST                       4: ans
                        996 ...`
- `
                        182     CONTAINS_OP                     0 (in)
                        184 ...`
- `
                858     MAKE_FUNCTION                   0
                860     STORE_NAME       ...`
- `
                        192     COMPARE_OP                      0 (<)
                        194  ...`
- `,)
                        8       CALL_FUNCTION_KW                2
                        10     ...`
- `,)
                        22      CALL_FUNCTION_KW                1
                        24     ...`
- `
                        92      LOAD_CONST                      5: `
- `
                        104     BINARY_ADD                      
                        106     CA...`
- `,)
                        8       CALL_FUNCTION_KW                2
                        10     ...`
- `
                30      RETURN_VALUE                    
        `
- `
                        244     STORE_FAST                      7: fracpart
                       ...`
- `
                332     MAKE_FUNCTION                   1
                334     STORE_NAME       ...`
- `
                        6       COMPARE_OP                      2 (==)
                        8   ...`
- `
                        106     LOAD_FAST                       0: self
                        108...`
- `,)
                        8       CALL_FUNCTION_KW                2
                        10     ...`
- `
                        180     STORE_FAST                      6: intpart
                        ...`
- Plus 437 more strings...

### pathlib_pycdas.dis

- `
                60      GET_ITER                        
                62      CALL_FUNCTION     ...`
- `
                        2       LOAD_METHOD                     0: format
                        4...`
- `
                134     MAKE_FUNCTION                   0
                136     STORE_NAME       ...`
- `
        390     MAKE_FUNCTION                   0
        392     LOAD_CONST                      3...`
- `
                        2       LOAD_METHOD                     0: format
                        4...`
- `
                        14      LOAD_FAST                       1: data
                        16 ...`
- `
        406     MAKE_FUNCTION                   0
        408     LOAD_CONST                      3...`
- `
                        12      CALL_METHOD                     1
                        14      P...`
- `
        362     MAKE_FUNCTION                   0
        364     LOAD_CONST                      2...`
- `,)
                        10      CALL_FUNCTION_KW                2
                        12     ...`
- `
                312     MAKE_FUNCTION                   0
                314     STORE_NAME       ...`
- `
                162     MAKE_FUNCTION                   0
                164     STORE_NAME       ...`
- `
                        18      DUP_TOP                         
                        20      ST...`
- `
                344     MAKE_FUNCTION                   0
                346     STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        44      LOAD_FAST                       0: self
                        46 ...`
- `
                24      MAKE_FUNCTION                   0
                26      STORE_NAME       ...`
- `
                114     MAKE_FUNCTION                   0
                116     STORE_NAME       ...`
- `
                        14      LOAD_CONST                      2: (`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- Plus 149 more strings...

### signal_pycdas.dis

- `
        84      LOAD_NAME                       7: __name__
        86      LOAD_CONST             ...`
- `
        100     MAKE_FUNCTION                   0
        102     STORE_NAME                      8...`
- `
        46      MAKE_FUNCTION                   0
        48      CALL_METHOD                     3...`
- `
                8       MAKE_FUNCTION                   8
                10      STORE_FAST       ...`
- `
        150     MAKE_FUNCTION                   0
        152     CALL_FUNCTION                   1...`
- `,)
        20      IMPORT_NAME                     1: enum
        22      IMPORT_FROM              ...`
- `
                36      CALL_METHOD                     1
                38      RETURN_VALUE     ...`
- `
        116     MAKE_FUNCTION                   0
        118     STORE_NAME                      1...`
- `
                14      CALL_METHOD                     1
                16      JUMP_IF_FALSE_OR_...`
- `
        228     MAKE_FUNCTION                   0
        230     CALL_FUNCTION                   1...`
- `valid_signals`
- `
        202     MAKE_FUNCTION                   0
        204     CALL_FUNCTION                   1...`
- `)
                4       CONTAINS_OP                     0 (in)
                6       RETURN_VALU...`
- `
                4       MAKE_FUNCTION                   0
                6       LOAD_GLOBAL      ...`
- `
                18      MAKE_FUNCTION                   0
                20      LOAD_FAST        ...`
- `)
                4       CONTAINS_OP                     0 (in)
                6       RETURN_VALU...`
- `
                4       MAKE_FUNCTION                   0
                6       LOAD_GLOBAL      ...`
- `
        176     MAKE_FUNCTION                   0
        178     CALL_FUNCTION                   1...`
- `
        64      MAKE_FUNCTION                   0
        66      CALL_METHOD                     3...`

### statistics_pycdas.dis

- `)
        148     IMPORT_NAME                     25: collections
        150     IMPORT_FROM       ...`
- `
        338     MAKE_FUNCTION                   2
        340     STORE_NAME                      4...`
- `,)
        234     LOAD_CONST                      28: <CODE> _fail_neg
        236     LOAD_CONST  ...`
- `
        170     LOAD_NAME                       28: ValueError
        172     CALL_FUNCTION       ...`
- `
                112     CALL_FUNCTION                   1
                114     RAISE_VARARGS    ...`
- `
                244     MAKE_FUNCTION                   0
                246     STORE_NAME       ...`
- `
        220     MAKE_FUNCTION                   0
        222     STORE_NAME                      3...`
- `
        422     MAKE_FUNCTION                   0
        424     STORE_NAME                      5...`
- `
                88      MAKE_FUNCTION                   1
                90      STORE_NAME       ...`
- `
                126     MAKE_FUNCTION                   0
                128     CALL_FUNCTION    ...`
- `
        396     MAKE_FUNCTION                   0
        398     STORE_NAME                      5...`
- `
                130     MAKE_FUNCTION                   8
                132     LOAD_FAST        ...`
- `
                28      CALL_FUNCTION                   1
                30      RAISE_VARARGS    ...`
- `
                        28      BUILD_STRING                    6
                        30      R...`
- `
                188     MAKE_FUNCTION                   0
                190     STORE_NAME       ...`
- `
                224     MAKE_FUNCTION                   0
                226     STORE_NAME       ...`
- `
                38      CALL_FUNCTION                   1
                40      LOAD_CONST       ...`
- `
        358     MAKE_FUNCTION                   1
        360     STORE_NAME                      5...`
- `
                80      MAKE_FUNCTION                   8
                82      LOAD_GLOBAL      ...`
- `,)
                10      CALL_FUNCTION_KW                3
                12      STORE_FAST     ...`
- Plus 60 more strings...

### ipaddress_pycdas.dis

- `
                26      CALL_FUNCTION                   1
                28      RAISE_VARARGS    ...`
- `
                68      MAKE_FUNCTION                   0
                70      STORE_NAME       ...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
                100     MAKE_FUNCTION                   0
                102     CALL_FUNCTION    ...`
- `
                        66      CALL_METHOD                     2
                        68      L...`
- `
                        20      BINARY_ADD                      
                        22      LO...`
- `
                122     CALL_FUNCTION                   1
                124     BUILD_LIST       ...`
- `
                104     MAKE_FUNCTION                   8
                106     STORE_NAME       ...`
- `
                160     MAKE_FUNCTION                   0
                162     CALL_FUNCTION    ...`
- `
                98      CALL_FUNCTION                   1
                100     LOAD_NAME        ...`
- `
                        88      LOAD_FAST                       3: exc
                        90  ...`
- `
                        10      CALL_METHOD                     1
                        12      L...`
- `
                        64      LOAD_FAST                       2: ip_int
                        6...`
- `
                126     MAKE_FUNCTION                   0
                128     CALL_FUNCTION    ...`
- `
                        108     LOAD_FAST                       6: exc
                        110 ...`
- `
                52      MAKE_FUNCTION                   8
                54      STORE_NAME       ...`
- `
        222     MAKE_FUNCTION                   0
        224     LOAD_CONST                      4...`
- `
        126     MAKE_FUNCTION                   0
        128     STORE_NAME                      1...`
- `
                98      MAKE_FUNCTION                   0
                100     CALL_FUNCTION    ...`
- `
                20      CALL_FUNCTION                   1
                22      STORE_NAME       ...`
- Plus 185 more strings...

### bz2_pycdas.dis

- ` not supported in binary mode"
                60      CALL_FUNCTION                   1
           ...`
- `,)
                14      LOAD_CONST                      3: 9
                16      LOAD_CONST  ...`
- `
                42      MAKE_FUNCTION                   0
                44      CALL_FUNCTION    ...`
- `
                24      MAKE_FUNCTION                   3
                26      STORE_NAME       ...`
- `
                76      MAKE_FUNCTION                   0
                78      STORE_NAME       ...`
- `
        108     MAKE_FUNCTION                   1
        110     STORE_NAME                      4...`
- `
                74      CALL_FUNCTION                   1
                76      RAISE_VARARGS    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        230     CALL_FUNCTION                   2
                        232     P...`
- `
                20      LOAD_FAST                       1: mode
                22      BUILD_TUPLE...`
- `
                96      MAKE_FUNCTION                   1
                98      STORE_NAME       ...`
- `
        14      STORE_NAME                      2: __author__
        16      LOAD_CONST           ...`
- `
                114     MAKE_FUNCTION                   0
                116     STORE_NAME       ...`
- `)
                        104     CONTAINS_OP                     0 (in)
                        106...`
- `
                2       LOAD_FAST                       1: mode
                4       CONTAINS_OP...`
- `
                        16      CALL_FUNCTION                   2
                        18      P...`
- `,)
                        280     CALL_FUNCTION_KW                3
                        282    ...`
- `
                150     MAKE_FUNCTION                   0
                152     STORE_NAME       ...`
- `)
        56      IMPORT_NAME                     9: _bz2
        58      IMPORT_FROM               ...`
- `
        90      LOAD_NAME                       8: _compression
        92      LOAD_ATTR          ...`
- Plus 12 more strings...

### webbrowser_pycdas.dis

- `
        66      MAKE_FUNCTION                   0
        68      LOAD_CONST                      5...`
- `
                        56      COMPARE_OP                      2 (==)
                        58  ...`
- `
                416     CALL_METHOD                     1
                418     POP_JUMP_IF_FALSE...`
- `
                        98      LOAD_FAST                       2: new
                        100 ...`
- `
        118     MAKE_FUNCTION                   1
        120     STORE_NAME                      1...`
- `
                22      MAKE_FUNCTION                   1
                24      STORE_NAME       ...`
- `
                10      COMPARE_OP                      2 (==)
                12      POP_JUMP_IF_...`
- `
                40      CALL_FUNCTION                   1
                42      CALL_FUNCTION    ...`
- `
                274     LOAD_GLOBAL                     6: Konqueror
                276     LOAD_G...`
- `
        280     MAKE_FUNCTION                   0
        282     LOAD_CONST                      3...`
- `
                50      MAKE_FUNCTION                   1
                52      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `)
                162     CALL_FUNCTION_KW                4
                164     POP_TOP         ...`
- `
        424     MAKE_FUNCTION                   0
        426     LOAD_CONST                      5...`
- `
                30      STORE_NAME                      6: remote_action
                32      LO...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        348     MAKE_FUNCTION                   0
        350     LOAD_CONST                      4...`
- `
                        14      MAKE_FUNCTION                   8
                        16      L...`
- `
                        46      CALL_METHOD                     2
                        48      S...`
- `,)
                196     CALL_FUNCTION_KW                2
                198     POP_TOP        ...`
- Plus 113 more strings...

### _strptime_pycdas.dis

- `)
                        160     LOAD_CONST                      26: (`
- `
                        90      BUILD_TUPLE                     2
                        92      L...`
- `
                1026    BINARY_SUBSCR                   
                1028    CALL_FUNCTION     ...`
- `
                        24      LOAD_FAST                       1: time_tuple
                     ...`
- `,)
        44      IMPORT_NAME                     4: re
        46      IMPORT_FROM                ...`
- `
                        272     STORE_FAST                      9: U_W
                        274 ...`
- `
                950     BINARY_SUBSCR                   
                952     LOAD_METHOD       ...`
- `
                        76      LOAD_CONST                      16: `
- `
                        4       MAKE_FUNCTION                   0
                        6       L...`
- `
                        272     LOAD_CONST                      45: `
- `)
        68      IMPORT_NAME                     10: datetime
        70      IMPORT_FROM          ...`
- `)
                66      CALL_FUNCTION_KW                2
                68      STORE_FAST      ...`
- `
                600     BINARY_SUBSCR                   
                602     LOAD_METHOD       ...`
- `
                        88      LOAD_CONST                      20: `
- `
                        58      LOAD_CONST                      10: `
- `
                        250     LOAD_GLOBAL                     0: time
                        252...`
- `
                854     COMPARE_OP                      2 (==)
                856     POP_JUMP_IF_...`
- `
                        50      LOAD_FAST                       3: time_tuple
                     ...`
- `
                1428    COMPARE_OP                      2 (==)
                1430    POP_JUMP_IF_...`
- `)
                1508    CONTAINS_OP                     1 (not in)
                1510    POP_JUM...`
- Plus 83 more strings...

### ast_pycdas.dis

- `
                        26      LOAD_FAST                       0: self
                        28 ...`
- `
                        44      CALL_METHOD                     2
                        46      S...`
- `
                698     LOAD_CONST                      166: `
- `
                548     MAKE_FUNCTION                   0
                550     STORE_NAME       ...`
- `
                162     MAKE_FUNCTION                   0
                164     STORE_NAME       ...`
- `
                182     MAKE_FUNCTION                   0
                184     STORE_NAME       ...`
- `
                                24      CALL_METHOD                     1
                         ...`
- `
        150     MAKE_FUNCTION                   0
        152     STORE_NAME                      1...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                230     MAKE_FUNCTION                   0
                232     STORE_NAME       ...`
- `,)
        84      BUILD_CONST_KEY_MAP             1
        86      LOAD_CONST                     ...`
- `
                10      STORE_FAST                      3: next_line
                12      LOAD_F...`
- `
                        54      CALL_METHOD                     1
                        56      P...`
- `
                814     LOAD_CONST                      189: `
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        12      CALL_METHOD                     1
                        14      P...`
- `
                        6       CALL_METHOD                     1
                        8       P...`
- `
                        14      LOAD_CONST                      2: `
- Plus 284 more strings...

### translate_pycdas.dis

- `
        42      STORE_NAME                      5: NV_DEFAULT_LOCALE
        44      LOAD_BUILD_CLA...`
- `
                        104     LOAD_FAST                       5: msg
                        106 ...`
- `,)
                        228     CALL_FUNCTION_KW                3
                        230    ...`
- `
                20      MAKE_FUNCTION                   0
                22      STORE_NAME       ...`
- `GeForce NOW`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        224     LOAD_CONST                      9: `
- `
        54      CALL_FUNCTION                   2
        56      STORE_NAME                      6...`
- `
                        84      BINARY_ADD                      
                        86      LO...`
- `
                                10      LOAD_FAST                       1: line
                   ...`
- `
                        26      CALL_METHOD                     2
                        28      S...`
- `
                        152     LOAD_CONST                      6: `
- `
        80      LOAD_CONST                      9: `
- `
                        48      MAKE_FUNCTION                   0
                        50      L...`
- `
                        124     LOAD_FAST                       5: msg
                        126 ...`
- `
        76      LOAD_CONST                      7: `
- `
                        174     BUILD_STRING                    2
                        176     C...`
- `
                        114     LOAD_CONST                      6: `
- `
                        44      LOAD_FAST                       1: e
                        46    ...`

### bisect_pycdas.dis

- `,)
                42      CALL_FUNCTION_KW                5
                44      STORE_FAST     ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                12      CALL_FUNCTION                   1
                14      RAISE_VARARGS    ...`
- `
        32      MAKE_FUNCTION                   3
        34      STORE_NAME                      2...`
- `
        48      MAKE_FUNCTION                   3
        50      STORE_NAME                      3...`
- `
        16      MAKE_FUNCTION                   3
        18      STORE_NAME                      1...`
- `
        64      MAKE_FUNCTION                   3
        66      STORE_NAME                      4...`
- `
                12      CALL_FUNCTION                   1
                14      RAISE_VARARGS    ...`

### _py_abc_pycdas.dis

- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        88      LOAD_CONST                      5: False
                        90...`
- `
                74      MAKE_FUNCTION                   0
                76      STORE_NAME       ...`
- `
                42      MAKE_FUNCTION                   1
                44      STORE_NAME       ...`
- `
                        4       LOAD_FAST                       0: cls
                        6   ...`
- `
                        14      CALL_FUNCTION                   1
                        16      R...`
- `
                        30      MAKE_FUNCTION                   0
                        32      L...`
- `
                        104     LOAD_FAST                       3: value
                        10...`
- `
                                18      LOAD_CONST                      1: False
                  ...`
- `
                58      MAKE_FUNCTION                   0
                60      STORE_NAME       ...`
- `
                24      MAKE_FUNCTION                   8
                26      STORE_NAME       ...`
- `
        26      MAKE_FUNCTION                   0
        28      LOAD_CONST                      5...`
- `
                        14      CALL_FUNCTION                   1
                        16      R...`
- `,)
                        24      CALL_FUNCTION_KW                2
                        26     ...`
- `,)
                        44      CALL_FUNCTION_KW                2
                        46     ...`
- `,)
        4       IMPORT_NAME                     0: _weakrefset
        6       IMPORT_FROM       ...`
- `
                        82      MAKE_FUNCTION                   8
                        84      L...`

### tempfile_pycdas.dis

- `
        330     MAKE_FUNCTION                   0
        332     STORE_NAME                      5...`
- `,)
                        38      CALL_FUNCTION_KW                2
                        40     ...`
- `
        346     MAKE_FUNCTION                   0
        348     STORE_NAME                      5...`
- `
        482     LOAD_NAME                       50: template
        484     LOAD_CONST            ...`
- `
                        12      MAKE_FUNCTION                   8
                        14      S...`
- `
                234     LOAD_FAST                       10: raw
                236     CALL_FUNCTI...`
- `
                88      CALL_FUNCTION                   2
                90      RAISE_VARARGS    ...`
- `
        164     MAKE_FUNCTION                   1
        166     STORE_NAME                      1...`
- `
                60      CALL_METHOD                     1
                62      LOAD_GLOBAL      ...`
- `,)
                        10      CALL_FUNCTION_KW                2
                        12     ...`
- `,)
                                94      CALL_FUNCTION_KW                2
                       ...`
- `, -1, None, None, None, None, None)
                24      LOAD_CONST                      6: None
...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
                92      MAKE_FUNCTION                   0
                94      STORE_NAME       ...`
- `
                        36      LOAD_METHOD                     6: format
                        3...`
- `)
                116     CALL_FUNCTION_KW                3
                118     STORE_FAST      ...`
- `, -1, None, None, None, None, None, True)
        532     LOAD_CONST                      3: None
  ...`
- `
                246     MAKE_FUNCTION                   0
                248     STORE_NAME       ...`
- `
        376     MAKE_FUNCTION                   0
        378     STORE_NAME                      5...`
- `TemporaryDirectory`
- Plus 74 more strings...

### optparse_pycdas.dis

- `
                230     MAKE_FUNCTION                   0
                232     STORE_NAME       ...`
- `)
                26      STORE_NAME                      6: STORE_ACTIONS
                28      L...`
- `
                58      MAKE_FUNCTION                   0
                60      STORE_NAME       ...`
- `
                        108     CALL_FUNCTION                   1
                        110     R...`
- `
                100     MAKE_FUNCTION                   0
                102     STORE_NAME       ...`
- `)
                16      LIST_EXTEND                     1
                18      STORE_NAME      ...`
- `
                        6       COMPARE_OP                      2 (==)
                        8   ...`
- `
                        48      LOAD_FAST                       2: mode
                        50 ...`
- `
                        84      COMPARE_OP                      2 (==)
                        86  ...`
- `
        244     MAKE_FUNCTION                   0
        246     LOAD_CONST                      3...`
- `
                26      MAKE_FUNCTION                   1
                28      STORE_NAME       ...`
- `
                        134     LOAD_FAST                       5: indent_first
                   ...`
- `
                        98      LOAD_FAST                       0: self
                        100...`
- `
                14      STORE_NAME                      4: NO_DEFAULT_VALUE
                16     ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        408     MAKE_FUNCTION                   0
        410     LOAD_CONST                      5...`
- `
        342     MAKE_FUNCTION                   0
        344     LOAD_CONST                      4...`
- `
        134     MAKE_FUNCTION                   0
        136     LOAD_CONST                      1...`
- `
                218     MAKE_FUNCTION                   0
                220     STORE_NAME       ...`
- `)
                        126     BUILD_CONST_KEY_MAP             2
                        128     ...`
- Plus 162 more strings...

### uu_pycdas.dis

- `
                8       COMPARE_OP                      2 (==)
                10      POP_JUMP_IF_...`
- `
                268     LOAD_GLOBAL                     16: os
                270     LOAD_ATTR   ...`
- `
                210     LOAD_FAST                       1: out_file
                212     FORMAT_...`
- `
                122     COMPARE_OP                      2 (==)
                124     POP_JUMP_IF_...`
- `
                14      LOAD_CONST                      4: (`
- `
                210     CALL_METHOD                     2
                212     STORE_FAST       ...`
- `
                96      LOAD_CONST                      7: 2
                98      CALL_METHOD   ...`
- `
                278     CALL_FUNCTION                   2
                280     POP_TOP          ...`
- `
        74      MAKE_FUNCTION                   1
        76      STORE_NAME                      8...`
- `
                292     BUILD_STRING                    3
                294     CALL_FUNCTION    ...`
- `
                176     STORE_FAST                      2: name
                178     LOAD_FAST  ...`
- `
                30      LOAD_CONST                      8: `
- `
                184     CALL_METHOD                     1
                186     LOAD_METHOD      ...`
- `
                210     CALL_FUNCTION                   2
                212     POP_TOP          ...`
- `
                586     CALL_FUNCTION                   1
                588     RAISE_VARARGS    ...`
- `
                52      LOAD_CONST                      15: `
- `
                10      COMPARE_OP                      2 (==)
                12      POP_JUMP_IF_...`
- `
        42      MAKE_FUNCTION                   0
        44      LOAD_CONST                      5...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                198     CALL_METHOD                     2
                200     STORE_FAST       ...`
- Plus 13 more strings...

### datetime_pycdas.dis

- `
                        18      LOAD_GLOBAL                     1: _DAYNAMES
                      ...`
- `
                50      MAKE_FUNCTION                   0
                52      CALL_FUNCTION    ...`
- `
                280     MAKE_FUNCTION                   0
                282     STORE_NAME       ...`
- `
                        50      CALL_FUNCTION                   1
                        52      R...`
- `
                        30      LOAD_FAST                       1: offset
                        3...`
- `
                288     LOAD_FAST                       12: sign
                290     LOAD_FAST ...`
- `
                        84      CALL_FUNCTION                   2
                        86      S...`
- `
                        126     FORMAT_VALUE                    4 (FVC_NONE | FVS_HAVE_SPEC)
      ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `)
                        40      CALL_FUNCTION_KW                5
                        42      ...`
- `
                        2       LOAD_FAST                       0: self
                        4  ...`
- `,)
                        104     CALL_FUNCTION_KW                6
                        106    ...`
- `
                270     MAKE_FUNCTION                   1
                272     STORE_NAME       ...`
- `
                        32      LOAD_FAST                       3: hh
                        34   ...`
- `,)
                        150     CALL_FUNCTION_KW                5
                        152    ...`
- `,)
                        24      CALL_FUNCTION_KW                1
                        26     ...`
- `
                232     MAKE_FUNCTION                   0
                234     STORE_NAME       ...`
- `
                        158     LOAD_FAST                       3: day
                        160 ...`
- `
                50      CALL_FUNCTION                   1
                52      RAISE_VARARGS    ...`
- `
                        124     CALL_FUNCTION                   1
                        126     R...`
- Plus 225 more strings...

### pickle_pycdas.dis

- `
                        4       LOAD_FAST                       0: self
                        6  ...`
- `
                        50      CALL_FUNCTION                   1
                        52      R...`
- `
                        104     LOAD_CONST                      0: None
                        106...`
- `
                956     MAKE_FUNCTION                   0
                958     STORE_NAME       ...`
- `,)
        52      IMPORT_NAME                     8: itertools
        54      IMPORT_FROM         ...`
- `
        788     MAKE_FUNCTION                   2
        790     STORE_NAME                      1...`
- `
                300     MAKE_FUNCTION                   0
                302     STORE_NAME       ...`
- `
                140     MAKE_FUNCTION                   0
                142     STORE_NAME       ...`
- `
                38      MAKE_FUNCTION                   0
                40      STORE_NAME       ...`
- `
                        52      LOAD_CONST                      4: `
- `
                        20      CALL_FUNCTION                   2
                        22      P...`
- `)
                40      CALL_FUNCTION_KW                3
                42      STORE_FAST      ...`
- `
        384     STORE_NAME                      53: PERSID
        386     LOAD_CONST              ...`
- `
                        28      LOAD_CONST                      0: None
                        30 ...`
- `
                688     MAKE_FUNCTION                   0
                690     STORE_NAME       ...`
- `
                996     MAKE_FUNCTION                   0
                998     STORE_NAME       ...`
- `
                        220     LOAD_FAST                       9: code
                        222...`
- `
                        6       COMPARE_OP                      2 (==)
                        8   ...`
- `
                        90      LOAD_FAST                       2: n
                        92    ...`
- `
                848     MAKE_FUNCTION                   0
                850     STORE_NAME       ...`
- Plus 223 more strings...

### copy_pycdas.dis

- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
        202     LOAD_CONST                      2: None
        204     CALL_FUNCTION              ...`
- `,)
        578     BUILD_CONST_KEY_MAP             1
        580     LOAD_CONST                     ...`
- `
        104     MAKE_FUNCTION                   0
        106     STORE_NAME                      1...`
- `
        492     MAKE_FUNCTION                   1
        494     STORE_NAME                      4...`
- `
                54      LOAD_CONST                      2: None
                56      CALL_FUNCTI...`
- `
                110     LOAD_CONST                      1: None
                112     CALL_FUNCTI...`
- `
                140     LOAD_CONST                      2: None
                142     CALL_FUNCTI...`
- `
        312     MAKE_FUNCTION                   0
        314     STORE_NAME                      4...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                26      MAKE_FUNCTION                   8
                28      LOAD_FAST        ...`
- `
        546     MAKE_FUNCTION                   0
        548     STORE_NAME                      4...`
- `
        38      MAKE_FUNCTION                   0
        40      LOAD_CONST                      5...`
- `,)
        58      IMPORT_NAME                     8: org.python.core
        60      IMPORT_FROM   ...`
- `
                10      MAKE_FUNCTION                   8
                12      LOAD_FAST        ...`
- `
                194     LOAD_CONST                      1: None
                196     CALL_FUNCTI...`

### install_pycdas.dis

- `
        848     MAKE_FUNCTION                   1
        850     STORE_NAME                      8...`
- `
                        380     LOAD_GLOBAL                     14: str
                        382...`
- `)
        326     CALL_FUNCTION_KW                3
        328     POP_TOP                         ...`
- `
        824     STORE_NAME                      83: ADDITIONAL_GAMEPAD_LAYOUT_FILE_CONTENT
        ...`
- `
                52      MAKE_FUNCTION                   0
                54      STORE_NAME       ...`
- `
                        600     LOAD_GLOBAL                     14: str
                        602...`
- `
                        74      CALL_METHOD                     1
                        76      P...`
- `
                        74      LOAD_CONST                      5: `
- `
                        6       CALL_METHOD                     1
                        8       P...`
- `
                        168     LOAD_CONST                      13: `
- `
                        106     LOAD_CONST                      3: `
- `
                        110     LOAD_FAST                       0: self
                        112...`
- `
        742     LOAD_CONST                      60: `
- `
                        212     LOAD_FAST                       1: e
                        214   ...`
- `
        522     BUILD_STRING                    2
        524     LOAD_NAME                       2...`
- `
                        216     BINARY_SUBSCR                   
                        218     ST...`
- `
                        142     COMPARE_OP                      2 (==)
                        144 ...`
- `
                        6       CALL_METHOD                     1
                        8       P...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        416     STORE_GLOBAL                    53: REPO
        418     LOAD_CONST                ...`
- Plus 225 more strings...

### selectors_pycdas.dis

- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                        44      LOAD_METHOD                     4: format
                        4...`
- `
                66      MAKE_FUNCTION                   0
                68      STORE_NAME       ...`
- `
        190     LOAD_NAME                       21: BaseSelector
        192     CALL_FUNCTION     ...`
- `
                44      MAKE_FUNCTION                   1
                46      STORE_NAME       ...`
- `
        80      MAKE_FUNCTION                   0
        82      STORE_NAME                      1...`
- `
                34      MAKE_FUNCTION                   0
                36      STORE_NAME       ...`
- `)
        92      LIST_EXTEND                     1
        94      CALL_FUNCTION                   ...`
- `
                32      MAKE_FUNCTION                   8
                34      STORE_NAME       ...`
- `
                84      MAKE_FUNCTION                   0
                86      CALL_FUNCTION    ...`
- `,)
        176     CALL_FUNCTION_KW                3
        178     STORE_NAME                     ...`
- `
                66      MAKE_FUNCTION                   1
                68      STORE_NAME       ...`
- `
        296     MAKE_FUNCTION                   0
        298     LOAD_CONST                      3...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                56      MAKE_FUNCTION                   8
                58      STORE_NAME       ...`
- `
                        42      BUILD_STRING                    2
                        44      C...`
- `
                46      MAKE_FUNCTION                   8
                48      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                64      MAKE_FUNCTION                   1
                66      STORE_NAME       ...`
- Plus 32 more strings...

### tokenize_pycdas.dis

- `
                        120     LOAD_FAST                       5: col_offset
                     ...`
- `
        226     LOAD_NAME                       29: Whitespace
        228     BINARY_ADD          ...`
- `
                44      MAKE_FUNCTION                   0
                46      LOAD_FAST        ...`
- `
                68      LOAD_CONST                      15: `
- `
                1534    CALL_METHOD                     1
                1536    POP_JUMP_IF_TRUE ...`
- `
                28      COMPARE_OP                      2 (==)
                30      POP_JUMP_IF_...`
- `
                6       CALL_FUNCTION                   2
                8       STORE_FAST       ...`
- `
                12      MAKE_FUNCTION                   0
                14      STORE_DEREF      ...`
- `
        744     LOAD_NAME                       73: Exception
        746     CALL_FUNCTION        ...`
- `
                        8       CALL_METHOD                     1
                        10      S...`
- `
                174     LOAD_FAST                       14: strstart
                176     CALL_F...`
- `
        348     MAKE_FUNCTION                   0
        350     STORE_NAME                      4...`
- `
        498     CALL_FUNCTION                   2
        500     BINARY_ADD                      
...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        792     MAKE_FUNCTION                   0
        794     STORE_NAME                      4...`
- `
                932     COMPARE_OP                      3 (!=)
                934     POP_JUMP_IF_...`
- `
        760     CALL_FUNCTION                   2
        762     STORE_NAME                      7...`
- `
                68      CALL_FUNCTION                   5
                70      YIELD_VALUE      ...`
- `
        10      STORE_NAME                      2: __credits__
        12      LOAD_CONST          ...`
- `)
                60      CALL_METHOD                     1
                62      POP_JUMP_IF_FALS...`
- Plus 84 more strings...

### argparse_pycdas.dis

- `
                26      MAKE_FUNCTION                   0
                28      STORE_NAME       ...`
- `
                        4       COMPARE_OP                      2 (==)
                        6   ...`
- `
                        8       LOAD_FAST                       1: text
                        10 ...`
- `
                132     MAKE_FUNCTION                   0
                134     STORE_NAME       ...`
- `
                        146     LOAD_CONST                      11: `
- `
                        178     LOAD_GLOBAL                     17: _VersionAction
                ...`
- `,)
                        652     CALL_FUNCTION_KW                2
                        654    ...`
- `
        390     LOAD_NAME                       32: Action
        392     CALL_FUNCTION           ...`
- `
                24      MAKE_FUNCTION                   0
                26      STORE_NAME       ...`
- `)
                        20      BUILD_CONST_KEY_MAP             2
                        22      ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       NOP...`
- `
                216     MAKE_FUNCTION                   0
                218     STORE_NAME       ...`
- `
                124     MAKE_FUNCTION                   1
                126     STORE_NAME       ...`
- `
                        22      LOAD_FAST                       1: help
                        24 ...`
- `
        438     LOAD_NAME                       32: Action
        440     CALL_FUNCTION           ...`
- `
        518     LOAD_NAME                       20: object
        520     CALL_FUNCTION           ...`
- `
                200     MAKE_FUNCTION                   0
                202     STORE_NAME       ...`
- `
                90      MAKE_FUNCTION                   0
                92      STORE_NAME       ...`
- `
                        130     LOAD_FAST                       3: get_metavar
                    ...`
- `
                        28      LOAD_FAST                       5: group
                        30...`
- Plus 284 more strings...

### string_pycdas.dis

- `
                        66      LOAD_FAST                       2: delim
                        68...`
- `
                78      MAKE_FUNCTION                   1
                80      STORE_NAME       ...`
- `
        58      STORE_NAME                      9: octdigits
        60      LOAD_CONST            ...`
- `
                        38      MAKE_FUNCTION                   8
                        40      S...`
- `
        86      MAKE_FUNCTION                   1
        88      STORE_NAME                      1...`
- `
                        52      LOAD_METHOD                     4: join
                        54 ...`
- `
                                76      CALL_METHOD                     1
                         ...`
- `
                6       LOAD_METHOD                     0: join
                8       LOAD_CONST ...`
- `
                        48      COMPARE_OP                      2 (==)
                        50  ...`
- `
                        12      CALL_FUNCTION                   1
                        14      R...`
- `
                20      MAKE_FUNCTION                   0
                22      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        30      STORE_NAME                      5: ascii_uppercase
        32      LOAD_NAME       ...`
- `
                        6       CALL_METHOD                     1
                        8       S...`
- `
                        84      CALL_FUNCTION                   1
                        86      R...`
- `
        22      STORE_NAME                      3: whitespace
        24      LOAD_CONST           ...`
- `
                38      MAKE_FUNCTION                   8
                40      STORE_NAME       ...`
- `
        48      BINARY_ADD                      
        50      LOAD_CONST                      9:...`
- `
        142     MAKE_FUNCTION                   0
        144     LOAD_CONST                      1...`
- Plus 15 more strings...

### fnmatch_pycdas.dis

- `
                104     CALL_FUNCTION                   1
                106     POP_TOP          ...`
- `
                294     COMPARE_OP                      2 (==)
                296     POP_JUMP_IF_...`
- `
                1064    LOAD_FAST                       2: res
                1066    FORMAT_VALUE...`
- `)
        84      CALL_FUNCTION_KW                2
        86      LOAD_CONST                      ...`
- `
                16      CALL_FUNCTION                   2
                18      STORE_FAST       ...`
- `
                414     INPLACE_ADD                     
                416     ROT_THREE         ...`
- `)
                644     CONTAINS_OP                     0 (in)
                646     POP_JUMP_IF...`
- `
                980     CALL_FUNCTION                   1
                982     POP_TOP          ...`
- `,)
        48      IMPORT_NAME                     6: itertools
        50      IMPORT_FROM         ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                534     MAKE_FUNCTION                   0
                536     LOAD_FAST        ...`
- `
                612     COMPARE_OP                      2 (==)
                614     POP_JUMP_IF_...`
- `
                        14      LOAD_CONST                      1: `
- `
                554     LOAD_FAST                       8: stuff
                556     CALL_METHO...`
- `
                274     LOAD_CONST                      13: `
- `translate`
- `
                588     COMPARE_OP                      2 (==)
                590     POP_JUMP_IF_...`
- `
                662     LOAD_FAST                       8: stuff
                664     FORMAT_VAL...`
- `
                        22      LOAD_CONST                      3: `
- `
        100     MAKE_FUNCTION                   0
        102     STORE_NAME                      1...`
- Plus 7 more strings...

### opcode_pycdas.dis

- `
        1286    LOAD_CONST                      230: 137
        1288    CALL_FUNCTION             ...`
- `
        352     LOAD_CONST                      58: 27
        354     CALL_FUNCTION               ...`
- `
        1016    LOAD_CONST                      186: 110
        1018    CALL_FUNCTION             ...`
- `
        632     LOAD_CONST                      114: 71
        634     CALL_FUNCTION              ...`
- `
        896     LOAD_CONST                      166: 100
        898     CALL_FUNCTION             ...`
- `
        1206    LOAD_CONST                      218: 130
        1208    CALL_FUNCTION             ...`
- `
        1420    LOAD_CONST                      250: 152
        1422    CALL_FUNCTION             ...`
- `
        1116    LOAD_CONST                      206: 121
        1118    CALL_FUNCTION             ...`
- `
        672     LOAD_CONST                      122: 75
        674     CALL_FUNCTION              ...`
- `
        1390    LOAD_CONST                      246: 147
        1392    CALL_FUNCTION             ...`
- `
        1440    LOAD_CONST                      254: 155
        1442    CALL_FUNCTION             ...`
- `
        1036    LOAD_CONST                      190: 112
        1038    CALL_FUNCTION             ...`
- `
        100
        `
- `)
        60      STORE_NAME                      6: cmp_op
        62      BUILD_LIST              ...`
- `
        512     LOAD_CONST                      90: 59
        514     CALL_FUNCTION               ...`
- `
        232     LOAD_CONST                      34: 11
        234     CALL_FUNCTION               ...`
- `
        836     LOAD_CONST                      154: 94
        838     CALL_FUNCTION              ...`
- `DICT_UPDATE`
- `
        432     LOAD_CONST                      74: 49
        434     CALL_FUNCTION               ...`
- `
        492     LOAD_CONST                      86: 56
        494     CALL_FUNCTION               ...`
- Plus 51 more strings...

### shutil_pycdas.dis

- `
        390     MAKE_FUNCTION                   0
        392     LOAD_CONST                      2...`
- `."
                206     LOAD_FAST                       0: src
                208     LOAD_FAST ...`
- `
        1058    BUILD_TUPLE                     4
        1060    LOAD_CONST                      1...`
- `
        950     MAKE_FUNCTION                   0
        952     STORE_NAME                      7...`
- `
                82      MAKE_FUNCTION                   8
                84      STORE_FAST       ...`
- `
        522     MAKE_FUNCTION                   0
        524     STORE_NAME                      4...`
- `
                150     CALL_FUNCTION                   2
                152     SETUP_WITH       ...`
- `
        584     MAKE_FUNCTION                   1
        586     STORE_NAME                      4...`
- `
                132     CALL_FUNCTION                   1
                134     RAISE_VARARGS    ...`
- `
        1198    CALL_METHOD                     2
        1200    STORE_NAME                      9...`
- `
        1288    MAKE_FUNCTION                   1
        1290    STORE_NAME                      9...`
- `
        1018    MAKE_FUNCTION                   0
        1020    STORE_NAME                      8...`
- `)
                276     GET_ITER                        
                278     FOR_ITER         ...`
- `
        1148    MAKE_FUNCTION                   0
        1150    STORE_NAME                      8...`
- `
        746     MAKE_FUNCTION                   0
        748     STORE_NAME                      6...`
- `
        550     MAKE_FUNCTION                   2
        552     STORE_NAME                      4...`
- `
                110     BINARY_ADD                      
                112     LOAD_FAST         ...`
- `
                42      LOAD_FAST                       0: filename
                44      BINARY_...`
- `
        616     CALL_FUNCTION                   2
        618     POP_JUMP_IF_FALSE               3...`
- `
                134     LOAD_FAST                       5: fn
                136     BINARY_MODULO...`
- Plus 120 more strings...

### contextlib_pycdas.dis

- `
                24      MAKE_FUNCTION                   0
                26      STORE_NAME       ...`
- `
        320     CALL_FUNCTION                   2
        322     STORE_NAME                      2...`
- `
        188     LOAD_NAME                       18: _GeneratorContextManagerBase
        190     LO...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                14      STORE_NAME                      4: _stream
                16      LOAD_CON...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                56      MAKE_FUNCTION                   0
                58      STORE_NAME       ...`
- `
                88      MAKE_FUNCTION                   0
                90      STORE_NAME       ...`
- `
        168     LOAD_NAME                       18: _GeneratorContextManagerBase
        170     LO...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                48      MAKE_FUNCTION                   0
                50      CALL_FUNCTION    ...`
- `
        210     MAKE_FUNCTION                   0
        212     STORE_NAME                      2...`
- `nullcontext`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
                24      MAKE_FUNCTION                   0
                26      STORE_NAME       ...`
- `
                24      MAKE_FUNCTION                   0
                26      STORE_NAME       ...`
- `
        304     LOAD_NAME                       13: AbstractContextManager
        306     CALL_FUN...`
- `
                        12      MAKE_FUNCTION                   8
                        14      S...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                18      MAKE_FUNCTION                   1
                20      STORE_NAME       ...`
- Plus 42 more strings...

### shlex_pycdas.dis

- `
                        472     LOAD_FAST                       0: self
                        474...`
- `
                2       LOAD_METHOD                     0: join
                4       LOAD_CONST ...`
- `"
                6       RETURN_VALUE                    
                8       LOAD_GLOBAL      ...`
- `
                        8       COMPARE_OP                      2 (==)
                        10  ...`
- `
                22      LOAD_GLOBAL                     2: repr
                24      LOAD_FAST  ...`
- `
                        246     STORE_FAST                      2: escapedstate
                   ...`
- `
                        30      LOAD_GLOBAL                     4: repr
                        32 ...`
- `
                        852     COMPARE_OP                      2 (==)
                        854 ...`
- `
                60      MAKE_FUNCTION                   0
                62      STORE_NAME       ...`
- `
                        74      LOAD_FAST                       0: self
                        76 ...`
- `
                        142     LOAD_FAST                       0: self
                        144...`
- `
                42      MAKE_FUNCTION                   0
                44      STORE_NAME       ...`
- `
                        1094    LOAD_FAST                       0: self
                        109...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `"
                32      LOAD_CONST                      4: `
- `
        80      MAKE_FUNCTION                   1
        82      STORE_NAME                      1...`
- ` to shlex.split() is deprecated."
                22      LOAD_GLOBAL                     2: Depreca...`
- `
                76      MAKE_FUNCTION                   0
                78      STORE_NAME       ...`
- `
                        86      LOAD_FAST                       0: self
                        88 ...`
- `
                        192     STORE_FAST                      4: punctuation_chars
              ...`
- Plus 29 more strings...

### _threading_local_pycdas.dis

- `,)
        20      IMPORT_NAME                     3: contextlib
        22      IMPORT_FROM        ...`
- `
        40      MAKE_FUNCTION                   0
        42      LOAD_CONST                      6...`
- `
        70      CALL_FUNCTION                   2
        72      STORE_NAME                      8...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        24      CALL_FUNCTION                   1
                        26      R...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
        54      MAKE_FUNCTION                   0
        56      CALL_FUNCTION                   1...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `\n\nSo, the separate thread:\n\n  >>> thread = threading.Thread(target=f)\n  >>> thread.start()\n  >...`
- `
                        36      MAKE_FUNCTION                   9
                        38      S...`
- `
                28      MAKE_FUNCTION                   0
                30      STORE_NAME       ...`
- `
                        2       LOAD_GLOBAL                     0: str
                        4   ...`
- `
                        4       COMPARE_OP                      2 (==)
                        6   ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `)
                14      STORE_NAME                      4: __slots__
                16      LOAD_...`
- `
                10      CALL_METHOD                     2
                12      STORE_FAST       ...`

### token_pycdas.dis

- `
        392     LOAD_NAME                       14: COMMA
        394     MAP_ADD                  ...`
- `
                28      CALL_METHOD                     1
                30      POP_JUMP_IF_TRUE ...`
- `
        344     LOAD_NAME                       9: LPAR
        346     MAP_ADD                    ...`
- `
        478     LOAD_NAME                       35: LEFTSHIFT
        480     MAP_ADD              ...`
- `ISEOF`
- `
        558     MAKE_FUNCTION                   0
        560     STORE_NAME                      7...`
- `
        442     LOAD_NAME                       50: DOUBLESLASHEQUAL
        444     MAP_ADD       ...`
- `
        430     LOAD_NAME                       19: SLASH
        432     MAP_ADD                  ...`
- `
        454     LOAD_NAME                       13: COLON
        456     MAP_ADD                  ...`
- `
        380     LOAD_NAME                       16: PLUS
        382     MAP_ADD                   ...`
- `
        280     MAKE_FUNCTION                   0
        282     LOAD_NAME                       6...`
- `
        490     LOAD_NAME                       31: LESSEQUAL
        492     MAP_ADD              ...`
- `
        466     LOAD_NAME                       15: SEMI
        468     MAP_ADD                   ...`
- `
        2       STORE_NAME                      0: __doc__
        4       BUILD_LIST              ...`
- `
        320     LOAD_NAME                       26: PERCENT
        322     MAP_ADD                ...`
- `
        418     LOAD_NAME                       25: DOT
        420     MAP_ADD                    ...`
- `
        332     LOAD_NAME                       21: AMPER
        334     MAP_ADD                  ...`
- `
        356     LOAD_NAME                       18: STAR
        358     MAP_ADD                   ...`
- `
        368     LOAD_NAME                       48: DOUBLESTAREQUAL
        370     MAP_ADD        ...`
- `
        514     LOAD_NAME                       32: GREATEREQUAL
        516     MAP_ADD           ...`
- Plus 2 more strings...

### gettext_pycdas.dis

- `
                        120     STORE_FAST                      12: ii
                        122 ...`
- `
                116     LOAD_GLOBAL                     5: _as_int
                118     BUILD_MA...`
- `
                22      MAKE_FUNCTION                   0
                24      STORE_NAME       ...`
- `
        364     MAKE_FUNCTION                   0
        366     STORE_NAME                      4...`
- `
                        378     CALL_METHOD                     1
                        380     G...`
- `
        284     MAKE_FUNCTION                   1
        286     STORE_NAME                      3...`
- `
                54      MAKE_FUNCTION                   0
                56      STORE_NAME       ...`
- `
                24      INPLACE_ADD                     
                26      STORE_FAST        ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        264     MAKE_FUNCTION                   1
        266     STORE_NAME                      3...`
- `,)
                24      CALL_FUNCTION_KW                4
                26      STORE_FAST     ...`
- `)
                12      CALL_FUNCTION_KW                4
                14      STORE_FAST      ...`
- `
                        14      LOAD_GLOBAL                     2: DeprecationWarning
             ...`
- `
                60      MAKE_FUNCTION                   0
                62      STORE_NAME       ...`
- `
                60      LOAD_FAST                       0: domain
                62      CALL_FUNC...`
- `
                48      COMPARE_OP                      2 (==)
                50      POP_JUMP_IF_...`
- `
                        642     CALL_METHOD                     1
                        644     S...`
- `
        60      LOAD_NAME                       2: re
        62      LOAD_ATTR                    ...`
- `
        118     LOAD_CONST                      17: `
- `
                60      LOAD_GLOBAL                     2: DeprecationWarning
                62   ...`
- Plus 78 more strings...

### dataclasses_pycdas.dis

- `
                        34      LOAD_FAST                       0: self
                        36 ...`
- `
                2       LOAD_FAST                       0: f
                4       LOAD_ATTR     ...`
- `
        126     MAKE_FUNCTION                   0
        128     LOAD_CONST                      7...`
- `
        366     MAKE_FUNCTION                   0
        368     STORE_NAME                      4...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        14      LOAD_FAST                       1: f
                        16    ...`
- `
                504     LOAD_FAST                       0: cls
                506     LOAD_ATTR   ...`
- `))
                788     GET_ITER                        
                790     FOR_ITER        ...`
- `
                22      STORE_FAST                      1: default
                24      JUMP_FOR...`
- `
                904     LOAD_FAST                       0: cls
                906     LOAD_ATTR   ...`
- `
                24      MAKE_FUNCTION                   8
                26      CALL_FUNCTION    ...`
- `
                6       MAKE_FUNCTION                   0
                8       LOAD_FAST        ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                12      LOAD_METHOD                     0: join
                14      LOAD_CLOSUR...`
- `
        382     MAKE_FUNCTION                   0
        384     STORE_NAME                      4...`
- `)
        352     BUILD_CONST_KEY_MAP             3
        354     LOAD_CONST                      ...`
- `
                150     BINARY_SUBSCR                   
                152     LOAD_CONST        ...`
- `
                4       MAKE_FUNCTION                   0
                6       LOAD_FAST        ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `)
                6       LOAD_CONST                      2: `
- Plus 137 more strings...

### csv_pycdas.dis

- `
                        34      LOAD_METHOD                     4: join
                        36 ...`
- `
        220     MAKE_FUNCTION                   0
        222     LOAD_CONST                      2...`
- `
                        90      BINARY_SUBSCR                   
                        92      LO...`
- `
                                14      STORE_NAME                      4: lineterminator
         ...`
- `
                        308     MAKE_FUNCTION                   0
                        310     L...`
- `
                30      STORE_NAME                      8: lineterminator
                32      L...`
- `
                        220     BINARY_SUBSCR                   
                        222     LO...`
- `
                18      MAKE_FUNCTION                   1
                20      STORE_NAME       ...`
- `
                        702     MAKE_FUNCTION                   0
                        704     L...`
- `
                50      MAKE_FUNCTION                   0
                52      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        118     CALL_FUNCTION                   2
        120     STORE_NAME                      1...`
- `
                50      MAKE_FUNCTION                   0
                52      STORE_NAME       ...`
- `
                14      STORE_NAME                      4: _name
                16      LOAD_CONST...`
- `
                        66      MAKE_FUNCTION                   8
                        68      L...`
- `
                14      STORE_NAME                      4: delimiter
                16      LOAD_C...`
- `
                18      MAKE_FUNCTION                   1
                20      STORE_NAME       ...`
- `
                        322     STORE_FAST                      14: delim
                        3...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                                6       STORE_NAME                      2: __qualname__
           ...`
- Plus 29 more strings...

### socket_pycdas.dis

- `
        428     LOAD_NAME                       26: errorTab
        430     LOAD_CONST            ...`
- `
        668     LOAD_NAME                       26: errorTab
        670     LOAD_CONST            ...`
- `
                114     MAKE_FUNCTION                   1
                116     STORE_NAME       ...`
- `
        1280    MAKE_FUNCTION                   0
        1282    LOAD_CONST                      2...`
- `
                94      MAKE_FUNCTION                   3
                96      STORE_NAME       ...`
- `
                        10      CALL_FUNCTION                   3
                        12      C...`
- `
                278     LOAD_NAME                       29: get_inheritable
                280    ...`
- `
        444     LOAD_NAME                       26: errorTab
        446     LOAD_CONST            ...`
- `
                64      CALL_FUNCTION                   1
                66      RAISE_VARARGS    ...`
- `
                48      MAKE_FUNCTION                   0
                50      STORE_NAME       ...`
- `
                14      CALL_METHOD                     1
                16      RETURN_VALUE     ...`
- `
        1180    CALL_FUNCTION                   2
        1182    POP_JUMP_IF_FALSE               6...`
- `
                        6       LOAD_CONST                      2: False
                        8 ...`
- `
                196     MAKE_FUNCTION                   8
                198     STORE_NAME       ...`
- `)
                16      CONTAINS_OP                     0 (in)
                18      POP_JUMP_IF...`
- `
        588     LOAD_NAME                       26: errorTab
        590     LOAD_CONST            ...`
- `)
                16      LIST_EXTEND                     1
                18      STORE_NAME      ...`
- `
        956     LOAD_NAME                       26: errorTab
        958     LOAD_CONST            ...`
- `
                        4       LOAD_FAST                       0: self
                        6  ...`
- `
        460     LOAD_NAME                       26: errorTab
        462     LOAD_CONST            ...`
- Plus 116 more strings...

### dis_pycdas.dis

- `
                148     CALL_METHOD                     1
                150     POP_TOP          ...`
- `
                        212     LOAD_METHOD                     12: join
                        21...`
- `
                22      LOAD_FAST                       0: argparse
                24      LOAD_ME...`
- `
                50      MAKE_FUNCTION                   0
                52      CALL_FUNCTION    ...`
- `
        196     LOAD_CONST                      30: `
- `
                8       CALL_FUNCTION                   2
                10      BUILD_TUPLE      ...`
- `
        280     LOAD_NAME                       33: _Instruction
        282     LOAD_ATTR         ...`
- `
        264     LOAD_NAME                       33: _Instruction
        266     LOAD_ATTR         ...`
- `
                286     CALL_METHOD                     1
                288     POP_TOP          ...`
- `,)
                14      CALL_FUNCTION_KW                1
                16      POP_TOP        ...`
- `
        192     LOAD_CONST                      28: `
- `)
                18      BUILD_CONST_KEY_MAP             2
                20      LOAD_CONST      ...`
- `
                240     CALL_METHOD                     1
                242     POP_TOP          ...`
- `
        188     LOAD_CONST                      26: `
- `
                368     LOAD_METHOD                     16: join
                370     LOAD_FAST ...`
- `
        406     MAKE_FUNCTION                   3
        408     STORE_NAME                      4...`
- `
                        68      CALL_METHOD                     1
                        70      P...`
- `,)
                8       CALL_FUNCTION_KW                2
                10      POP_TOP        ...`
- `
                18      MAKE_FUNCTION                   1
                20      STORE_NAME       ...`
- `
        390     MAKE_FUNCTION                   1
        392     STORE_NAME                      4...`
- Plus 67 more strings...

### _compression_pycdas.dis

- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                54      MAKE_FUNCTION                   0
                56      STORE_NAME       ...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
                        14      CALL_METHOD                     1
                        16      R...`
- `DecompressReader`
- `
                        14      CALL_METHOD                     1
                        16      R...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                38      MAKE_FUNCTION                   8
                40      STORE_NAME       ...`
- `
        36      LOAD_NAME                       1: io
        38      LOAD_ATTR                    ...`
- `
                        28      RETURN_VALUE                    
                        30      LO...`
- `
                72      MAKE_FUNCTION                   0
                74      STORE_NAME       ...`
- `
                        166     STORE_FAST                      3: rawblock
                       ...`
- `
                94      MAKE_FUNCTION                   1
                96      STORE_NAME       ...`
- `
                        96      LOAD_METHOD                     9: format
                        9...`
- `
                        16      CALL_METHOD                     1
                        18      S...`
- `
                        10      CALL_FUNCTION                   1
                        12      R...`
- `
                        48      LOAD_METHOD                     4: join
                        50 ...`

### calendar_pycdas.dis

- `
                294     COMPARE_OP                      2 (==)
                296     POP_JUMP_IF_...`
- `
                        250     MAKE_FUNCTION                   8
                        252     L...`
- `
                178     LOAD_CONST                      34: `
- `
                60      MAKE_FUNCTION                   0
                62      STORE_NAME       ...`
- `
                        28      MAKE_FUNCTION                   8
                        30      L...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                        14      LOAD_FAST                       0: self
                        16 ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        14      LOAD_CONST                      2: (`
- `
                126     LOAD_CONST                      24: `
- `
        292     MAKE_FUNCTION                   0
        294     LOAD_CONST                      4...`
- `
                        2       LOAD_FAST                       0: self
                        4  ...`
- `
                54      MAKE_FUNCTION                   0
                56      STORE_NAME       ...`
- `
                216     LOAD_GLOBAL                     4: int
                218     LOAD_CONST  ...`
- `)
                16      LIST_EXTEND                     1
                18      STORE_NAME      ...`
- `
                        124     CALL_FUNCTION                   1
                        126     P...`
- `
                112     MAKE_FUNCTION                   1
                114     STORE_NAME       ...`
- `,)
                486     CALL_FUNCTION_KW                1
                488     STORE_FAST     ...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
                198     LOAD_GLOBAL                     4: int
                200     LOAD_CONST  ...`
- Plus 105 more strings...

### lzma_pycdas.dis

- `
                144     MAKE_FUNCTION                   1
                146     STORE_NAME       ...`
- ` not supported in binary mode"
                60      CALL_FUNCTION                   1
           ...`
- `
                30      MAKE_FUNCTION                   3
                32      STORE_NAME       ...`
- `
                66      MAKE_FUNCTION                   0
                68      STORE_NAME       ...`
- `)
                        112     CALL_FUNCTION_KW                4
                        114     ...`
- `
                122     MAKE_FUNCTION                   1
                124     STORE_NAME       ...`
- `
                48      MAKE_FUNCTION                   0
                50      CALL_FUNCTION    ...`
- `,)
        40      IMPORT_NAME                     5: _lzma
        42      IMPORT_STAR             ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `)
                        22      CONTAINS_OP                     0 (in)
                        24 ...`
- `,)
        100     LOAD_CONST                      3: None
        102     LOAD_CONST               ...`
- `)
                108     CALL_FUNCTION_KW                6
                110     STORE_FAST      ...`
- `
                78      CALL_FUNCTION                   1
                80      RAISE_VARARGS    ...`
- `
                2       LOAD_FAST                       1: mode
                4       CONTAINS_OP...`
- `
                82      MAKE_FUNCTION                   0
                84      STORE_NAME       ...`
- `
                        208     CALL_FUNCTION                   2
                        210     P...`
- `
                        54      CALL_FUNCTION                   1
                        56      R...`
- `
        86      MAKE_FUNCTION                   0
        88      LOAD_CONST                      9...`
- `
                102     MAKE_FUNCTION                   1
                104     STORE_NAME       ...`
- `
                        240     CALL_FUNCTION                   1
                        242     R...`
- Plus 7 more strings...

### numbers_pycdas.dis

- `
                92      MAKE_FUNCTION                   0
                94      CALL_FUNCTION    ...`
- `
                22      MAKE_FUNCTION                   0
                24      CALL_FUNCTION    ...`
- `
                186     MAKE_FUNCTION                   0
                188     STORE_NAME       ...`
- `
        120     MAKE_FUNCTION                   0
        122     LOAD_CONST                      1...`
- `
                234     MAKE_FUNCTION                   0
                236     CALL_FUNCTION    ...`
- `
        78      MAKE_FUNCTION                   0
        80      LOAD_CONST                      1...`
- `
                22      MAKE_FUNCTION                   0
                24      CALL_FUNCTION    ...`
- `
                98      MAKE_FUNCTION                   0
                100     CALL_FUNCTION    ...`
- `
                162     MAKE_FUNCTION                   0
                164     CALL_FUNCTION    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                44      MAKE_FUNCTION                   0
                46      CALL_FUNCTION    ...`
- `
                52      MAKE_FUNCTION                   0
                54      STORE_NAME       ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                160     MAKE_FUNCTION                   0
                162     CALL_FUNCTION    ...`
- `
                44      MAKE_FUNCTION                   1
                46      CALL_FUNCTION    ...`
- `
                180     MAKE_FUNCTION                   0
                182     CALL_FUNCTION    ...`
- `
                140     MAKE_FUNCTION                   0
                142     CALL_FUNCTION    ...`
- `
                116     MAKE_FUNCTION                   0
                118     CALL_FUNCTION    ...`
- `
                136     MAKE_FUNCTION                   0
                138     CALL_FUNCTION    ...`
- `
                164     MAKE_FUNCTION                   0
                166     CALL_FUNCTION    ...`
- Plus 19 more strings...

### tracemalloc_pycdas.dis

- `
                26      MAKE_FUNCTION                   0
                28      CALL_FUNCTION    ...`
- `
                34      MAKE_FUNCTION                   0
                36      CALL_FUNCTION    ...`
- `)
                        4       CONTAINS_OP                     1 (not in)
                       ...`
- `
                        80      LOAD_FAST                       5: frame
                        82...`
- `
                        2       LOAD_FAST                       0: self
                        4  ...`
- `)
        4       IMPORT_NAME                     0: collections.abc
        6       IMPORT_FROM    ...`
- `
                52      MAKE_FUNCTION                   0
                54      STORE_NAME       ...`
- `
                54      MAKE_FUNCTION                   0
                56      CALL_FUNCTION    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                70      MAKE_FUNCTION                   1
                72      STORE_NAME       ...`
- `
                        14      LOAD_GLOBAL                     3: type
                        16 ...`
- `
                50      MAKE_FUNCTION                   0
                52      STORE_NAME       ...`
- `
        184     CALL_FUNCTION                   2
        186     STORE_NAME                      2...`
- `,)
                14      STORE_NAME                      4: __slots__
                16      LOAD...`
- `)
                14      STORE_NAME                      4: __slots__
                16      LOAD_...`
- `
                        6       CALL_FUNCTION                   2
                        8       S...`
- `take_snapshot`
- `
                44      MAKE_FUNCTION                   0
                46      STORE_NAME       ...`
- `
                        40      LOAD_FAST                       0: self
                        42 ...`
- `
                98      MAKE_FUNCTION                   0
                100     STORE_NAME       ...`
- Plus 60 more strings...

### base64_pycdas.dis

- `
                104     MAKE_FUNCTION                   8
                106     LOAD_GLOBAL      ...`
- `
                264     CALL_FUNCTION                   1
                266     RAISE_VARARGS    ...`
- `
                164     LOAD_METHOD                     8: join
                166     LOAD_FAST  ...`
- `
                12      MAKE_FUNCTION                   0
                14      LOAD_GLOBAL      ...`
- `
                150     COMPARE_OP                      2 (==)
                152     POP_JUMP_IF_...`
- `
                68      LOAD_METHOD                     7: join
                70      LOAD_FAST  ...`
- `
        226     MAKE_FUNCTION                   0
        228     STORE_NAME                      3...`
- `
        96      CALL_METHOD                     2
        98      STORE_NAME                      1...`
- `
        284     MAKE_FUNCTION                   1
        286     STORE_NAME                      3...`
- `
                210     LOAD_FAST                       1: i
                212     LOAD_FAST     ...`
- `
        108     CALL_METHOD                     2
        110     STORE_NAME                      1...`
- `
        84      MAKE_FUNCTION                   0
        86      STORE_NAME                      1...`
- `
                        18      JUMP_FORWARD                    27 (to 74)
                        ...`
- `
        124     MAKE_FUNCTION                   0
        126     STORE_NAME                      1...`
- `
                60      CALL_METHOD                     2
                62      CALL_METHOD      ...`
- `
                292     LOAD_FAST                       3: encoded
                294     LOAD_CON...`
- `
                26      LOAD_FAST                       0: s
                28      CALL_METHOD   ...`
- `
                348     CALL_METHOD                     2
                350     STORE_FAST       ...`
- `
                70      LOAD_FAST                       3: padding
                72      BINARY_M...`
- `
                12      MAKE_FUNCTION                   0
                14      LOAD_GLOBAL      ...`
- Plus 46 more strings...

### decimal_pycdas.dis

- `,)
        26      IMPORT_NAME                     0: _decimal
        28      IMPORT_FROM          ...`
- `,)
        68      IMPORT_NAME                     5: _pydecimal
        70      IMPORT_STAR        ...`
- `,)
        88      IMPORT_NAME                     5: _pydecimal
        90      IMPORT_FROM        ...`
- `,)
        6       IMPORT_NAME                     0: _decimal
        8       IMPORT_STAR          ...`

### quopri_pycdas.dis

- `
                48      LOAD_FAST                       0: c
                50      DUP_TOP       ...`
- `
                64      LOAD_FAST                       0: c
                66      DUP_TOP       ...`
- `,)
                304     CALL_FUNCTION_KW                2
                306     POP_TOP        ...`
- `
        136     MAKE_FUNCTION                   0
        138     STORE_NAME                      1...`
- `
        26      STORE_NAME                      5: EMPTYSTRING
        28      SETUP_FINALLY       ...`
- `,)
                24      CALL_FUNCTION_KW                2
                26      STORE_FAST     ...`
- `)
                18      CALL_FUNCTION_KW                3
                20      RETURN_VALUE    ...`
- `
                40      LOAD_FAST                       0: c
                42      DUP_TOP       ...`
- `
                36      CALL_METHOD                     2
                38      UNPACK_SEQUENCE  ...`
- `
                96      LOAD_FAST                       2: c
                98      DUP_TOP       ...`
- `
                226     BINARY_ADD                      
                228     STORE_FAST        ...`
- `
                18      CONTAINS_OP                     0 (in)
                20      POP_JUMP_IF_...`
- `
                394     COMPARE_OP                      3 (!=)
                396     POP_JUMP_IF_...`
- `
        14      STORE_NAME                      2: ESCAPE
        16      LOAD_CONST               ...`
- `)
                26      CALL_FUNCTION_KW                3
                28      STORE_FAST      ...`
- `
        80      MAKE_FUNCTION                   0
        82      STORE_NAME                      1...`
- `
        118     MAKE_FUNCTION                   1
        120     STORE_NAME                      1...`
- `
                        16      CONTAINS_OP                     0 (in)
                        18  ...`
- `
                242     COMPARE_OP                      2 (==)
                244     POP_JUMP_IF_...`
- `
        152     MAKE_FUNCTION                   0
        154     STORE_NAME                      1...`
- Plus 20 more strings...

### py_compile_pycdas.dis

- `,)
                134     CALL_FUNCTION_KW                2
                136     POP_TOP        ...`
- `
                10      STORE_FAST                      1: description
                12      LOAD...`
- `
                8       CALL_METHOD                     1
                10      POP_JUMP_IF_FALSE...`
- `
        82      MAKE_FUNCTION                   0
        84      LOAD_CONST                      5...`
- `
                258     BINARY_ADD                      
                260     CALL_METHOD       ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                90      STORE_FAST                      8: msg
                92      LOAD_GLOBAL ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                376     BINARY_SUBSCR                   
                378     CALL_METHOD       ...`
- `
                34      LOAD_CONST                      7: `
- `
                50      LOAD_CONST                      11: `
- `)
                54      CALL_FUNCTION_KW                3
                56      POP_TOP         ...`
- `
                26      MAKE_FUNCTION                   0
                28      STORE_NAME       ...`
- `
                        40      LOAD_FAST                       3: file
                        42 ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                44      STORE_FAST                      7: optimization
                46      LOA...`
- `
        136     MAKE_FUNCTION                   0
        138     STORE_NAME                      1...`
- `
        98      MAKE_FUNCTION                   0
        100     LOAD_CONST                      7...`
- `
        114     MAKE_FUNCTION                   0
        116     STORE_NAME                      1...`
- `,)
                14      LOAD_CONST                      3: <CODE> __init__
                16    ...`
- Plus 6 more strings...

### pprint_pycdas.dis

- `
                        138     CALL_FUNCTION                   1
                        140     P...`
- `
                304     MAKE_FUNCTION                   0
                306     STORE_NAME       ...`
- `
                30      MAKE_FUNCTION                   0
                32      STORE_NAME       ...`
- `,)
                        232     CALL_FUNCTION_KW                2
                        234    ...`
- `
                2       LOAD_GLOBAL                     0: type
                4       LOAD_FAST  ...`
- `
                222     MAKE_FUNCTION                   0
                224     STORE_NAME       ...`
- `
                        70      CALL_FUNCTION                   1
                        72      P...`
- `
                        16      STORE_FAST                      7: cls_name
                       ...`
- `
                24      MAKE_FUNCTION                   3
                26      STORE_NAME       ...`
- `
                        38      BINARY_MULTIPLY                 
                        40      CA...`
- ` repr()-like value, but protect against recursive\n    data structures.\n\n"
        2       STORE_N...`
- `
                        18      LOAD_CONST                      2: `
- `
                120     LOAD_FAST                       5: t3
                122     LOAD_FAST    ...`
- `, True, False)
                        430     RETURN_VALUE                    
                    ...`
- `
                        64      CALL_FUNCTION                   1
                        66      R...`
- `
                        452     STORE_FAST                      21: format
                        ...`
- `
                        36      LOAD_CONST                      0: None
                        38 ...`
- `
                288     MAKE_FUNCTION                   0
                290     STORE_NAME       ...`
- `
                40      MAKE_FUNCTION                   0
                42      STORE_NAME       ...`
- `
                        402     LOAD_FAST                       3: indent
                        4...`
- Plus 65 more strings...

### glob_pycdas.dis

- `
                24      MAKE_FUNCTION                   0
                26      LOAD_FAST        ...`
- `,)
                32      CALL_FUNCTION_KW                2
                34      POP_TOP        ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `)
        76      BUILD_CONST_KEY_MAP             3
        78      LOAD_CONST                      ...`
- `
        156     MAKE_FUNCTION                   0
        158     STORE_NAME                      1...`
- `
        240     MAKE_FUNCTION                   0
        242     STORE_NAME                      2...`
- `
        124     MAKE_FUNCTION                   0
        126     STORE_NAME                      1...`
- `,)
                32      CALL_FUNCTION_KW                2
                34      STORE_FAST     ...`
- `
                32      LOAD_FAST                       0: pathname
                34      CALL_ME...`
- `
        206     CALL_METHOD                     1
        208     STORE_NAME                      2...`
- `,)
                36      CALL_FUNCTION_KW                3
                38      DUP_TOP        ...`
- `
        108     MAKE_FUNCTION                   0
        110     STORE_NAME                      1...`
- `)
                14      CALL_FUNCTION_KW                4
                16      CALL_FUNCTION   ...`
- `
        224     MAKE_FUNCTION                   0
        226     STORE_NAME                      2...`
- `
        172     MAKE_FUNCTION                   0
        174     STORE_NAME                      1...`
- `, 46)
                8       CONTAINS_OP                     0 (in)
                10      RETURN_...`
- `
                14      COMPARE_OP                      2 (==)
                16      RETURN_VALUE...`
- `
        140     MAKE_FUNCTION                   0
        142     STORE_NAME                      1...`
- `)
        94      BUILD_CONST_KEY_MAP             3
        96      LOAD_CONST                      ...`
- `O_DIRECTORY`
- Plus 2 more strings...

### install_ui_pycdas.dis

- `
                14      STORE_NAME                      4: title_fg
                16      LOAD_CO...`
- `
        78      CALL_FUNCTION                   2
        80      STORE_NAME                      1...`
- `
                        422     LOAD_FAST                       0: self
                        424...`
- `
                        106     LOAD_CONST                      5: 20
                        108  ...`
- `
                        46      LOAD_CONST                      6: (`
- `
                        40      LOAD_CONST                      2: `
- `
                        164     LOAD_FAST                       6: x
                        166   ...`
- `
                        230     CALL_METHOD                     3
                        232     L...`
- `
                        60      LOAD_CONST                      8: (`
- `
                        134     LOAD_CONST                      9: 520
                        136 ...`
- `)
                        260     CALL_FUNCTION_KW                9
                        262     ...`
- `
                86      MAKE_FUNCTION                   0
                88      STORE_NAME       ...`
- `
                        138     LOAD_CONST                      12: `
- `
                        52      LOAD_FAST                       2: x
                        54    ...`
- `,)
                        236     CALL_FUNCTION_KW                2
                        238    ...`
- `
                        172     LOAD_FAST                       1: title
                        17...`
- `)
                        382     CALL_FUNCTION_KW                3
                        384     ...`
- `
                        42      CALL_METHOD                     3
                        44      L...`
- `
                        74      CALL_METHOD                     3
                        76      L...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- Plus 50 more strings...

### platform_pycdas.dis

- `
                22      CONTAINS_OP                     1 (not in)
                24      POP_JUMP...`
- `
                2       LOAD_METHOD                     0: join
                4       LOAD_CONST ...`
- `
                238     COMPARE_OP                      2 (==)
                240     POP_JUMP_IF_...`
- `
                56      LOAD_CONST                      1: `
- `,)
                170     CONTAINS_OP                     0 (in)
                172     POP_JUMP_I...`
- `
                422     STORE_FAST                      11: branch
                424     LOAD_CON...`
- `
        366     MAKE_FUNCTION                   0
        368     LOAD_CONST                      7...`
- `
                68      LOAD_CONST                      1: `
- `
                        40      LOAD_CONST                      1: 0
                        42    ...`
- `
                70      STORE_FAST                      1: cvkey
                72      LOAD_FAST ...`
- `
                170     COMPARE_OP                      2 (==)
                172     POP_JUMP_IF_...`
- `
                110     COMPARE_OP                      0 (<)
                112     POP_JUMP_IF_F...`
- `
        206     LOAD_CONST                      41: `
- `
                152     COMPARE_OP                      2 (==)
                154     POP_JUMP_IF_...`
- `
                32      CALL_METHOD                     1
                34      STORE_FAST       ...`
- `
                134     LOAD_CONST                      5: `
- `
        300     MAKE_FUNCTION                   1
        302     STORE_NAME                      3...`
- `)
        328     LOAD_CONST                      23: (`
- `
        348     MAKE_FUNCTION                   1
        350     STORE_NAME                      3...`
- `
        400     CALL_METHOD                     2
        402     CALL_FUNCTION                   3...`
- Plus 139 more strings...

### subprocess_pycdas.dis

- `
                        418     LOAD_FAST                       30: k
                        420  ...`
- `
                18      MAKE_FUNCTION                   1
                20      STORE_NAME       ...`
- `
                62      CALL_METHOD                     1
                64      LOAD_CONST       ...`
- `)
        308     LIST_EXTEND                     1
        310     CALL_METHOD                     ...`
- `
                        24      LOAD_FAST                       0: self
                        26 ...`
- `
                        78      CALL_FUNCTION                   1
                        80      R...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                        186     STORE_SUBSCR                    
                        188     LO...`
- `
                10      CALL_FUNCTION                   2
                12      POP_JUMP_IF_TRUE ...`
- `
                282     MAKE_FUNCTION                   0
                284     STORE_NAME       ...`
- `,)
                        28      CALL_FUNCTION_KW                1
                        30     ...`
- `
        416     CALL_FUNCTION                   2
        418     POP_JUMP_IF_FALSE               2...`
- `
                448     MAKE_FUNCTION                   0
                450     STORE_NAME       ...`
- `
                        520     CALL_FUNCTION                   1
                        522     R...`
- `
        502     MAKE_FUNCTION                   2
        504     STORE_NAME                      6...`
- `
                36      MAKE_FUNCTION                   0
                38      CALL_FUNCTION    ...`
- `
        340     LOAD_NAME                       44: SubprocessError
        342     CALL_FUNCTION  ...`
- `
                        8       CALL_FUNCTION                   1
                        10      R...`
- `,)
                        326     CALL_FUNCTION_KW                1
                        328    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- Plus 135 more strings...

### tarfile_pycdas.dis

- `
                        120     LOAD_CONST                      5: `
- `
                        248     CALL_METHOD                     2
                        250     L...`
- `
                108     LOAD_CONST                      8: `
- `
        10      STORE_NAME                      2: __author__
        12      LOAD_CONST           ...`
- `
                        56      COMPARE_OP                      2 (==)
                        58  ...`
- `
                        340     CALL_FUNCTION                   1
                        342     L...`
- `
                        146     CALL_FUNCTION                   1
                        148     L...`
- `
                140     LOAD_CONST                      18: `
- `
                468     MAKE_FUNCTION                   0
                470     STORE_NAME       ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                542     CALL_METHOD                     2
                544     SETUP_WITH       ...`
- `
                        18      BINARY_SUBSCR                   
                        20      LO...`
- `
                8       CALL_FUNCTION                   2
                10      POP_JUMP_IF_FALSE...`
- `
                298     MAKE_FUNCTION                   0
                300     CALL_FUNCTION    ...`
- `
                        24      COMPARE_OP                      2 (==)
                        26  ...`
- `
                        352     CALL_FUNCTION                   1
                        354     L...`
- `
                        162     CALL_FUNCTION                   1
                        164     R...`
- `
        320     STORE_NAME                      47: XGLTYPE
        322     LOAD_CONST             ...`
- `
                6       CALL_METHOD                     1
                8       STORE_FAST       ...`
- `
                        274     CALL_FUNCTION                   1
                        276     R...`
- Plus 352 more strings...

### stringprep_pycdas.dis

- `
        294     MAP_ADD                         1
        296     LOAD_CONST                      8...`
- `
        1838    MAP_ADD                         1
        1840    LOAD_CONST                      4...`
- `
        206     MAP_ADD                         1
        208     LOAD_CONST                      5...`
- `
        1854    MAP_ADD                         1
        1856    LOAD_CONST                      4...`
- `
        1098    MAP_ADD                         1
        1100    LOAD_CONST                      2...`
- `
        5534    MAP_ADD                         1
        5536    LOAD_CONST                      8...`
- `
        4548    MAP_ADD                         1
        4550    LOAD_CONST                      7...`
- `
        4414    MAP_ADD                         1
        4416    LOAD_CONST                      6...`
- `
        4508    MAP_ADD                         1
        4510    LOAD_CONST                      7...`
- `
        218     MAP_ADD                         1
        220     LOAD_CONST                      5...`
- `
        194     MAP_ADD                         1
        196     LOAD_CONST                      5...`
- `
        3510    MAP_ADD                         1
        3512    LOAD_CONST                      5...`
- `
        4766    MAP_ADD                         1
        4768    LOAD_CONST                      7...`
- `
        4472    MAP_ADD                         1
        4474    LOAD_CONST                      7...`
- `
        5224    MAP_ADD                         1
        5226    LOAD_CONST                      7...`
- `
        2020    MAP_ADD                         1
        2022    LOAD_CONST                      4...`
- `)
                10      CONTAINS_OP                     0 (in)
                12      RETURN_VALU...`
- `
        518     MAP_ADD                         1
        520     LOAD_CONST                      1...`
- `
        1928    MAP_ADD                         1
        1930    LOAD_CONST                      4...`
- `
        2146    MAP_ADD                         1
        2148    LOAD_CONST                      4...`
- Plus 326 more strings...

### typing_pycdas.dis

- `
                        4       LOAD_METHOD                     1: format
                        6...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `)
                36      CALL_FUNCTION_KW                3
                38      RETURN_VALUE    ...`
- `
                66      LOAD_NAME                       11: Optional
                68      LOAD_N...`
- `
        1866    LOAD_NAME                       76: Protocol
        1868    CALL_FUNCTION         ...`
- `
        490     LOAD_NAME                       32: _Final
        492     LOAD_NAME               ...`
- `
                        136     LOAD_FAST                       0: cls
                        138 ...`
- `
                54      MAKE_FUNCTION                   4
                56      CALL_FUNCTION    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                52      MAKE_FUNCTION                   0
                54      STORE_NAME       ...`
- `
                56      MAKE_FUNCTION                   8
                58      LOAD_FAST        ...`
- `
                44      MAKE_FUNCTION                   0
                46      STORE_NAME       ...`
- `
        984     MAKE_FUNCTION                   0
        986     STORE_NAME                      8...`
- `
                        160     LOAD_FAST                       4: base
                        162...`
- `
                62      STORE_SUBSCR                    
                64      POP_BLOCK         ...`
- `
        186     MAKE_FUNCTION                   0
        188     STORE_NAME                      2...`
- `,)
        522     CALL_FUNCTION_KW                5
        524     STORE_NAME                     ...`
- `
                234     MAKE_FUNCTION                   5
                236     CALL_FUNCTION    ...`
- `)
                18      BUILD_CONST_KEY_MAP             2
                20      LOAD_CONST      ...`
- `
                28      MAKE_FUNCTION                   10
                30      STORE_NAME      ...`
- Plus 345 more strings...

### zipfile_pycdas.dis

- `
                20      MAKE_FUNCTION                   0
                22      STORE_NAME       ...`
- `
        1006    MAKE_FUNCTION                   0
        1008    STORE_NAME                      1...`
- `
                56      MAKE_FUNCTION                   0
                58      STORE_NAME       ...`
- `
        806     MAP_ADD                         1
        808     LOAD_CONST                      2...`
- `
                28      CALL_FUNCTION                   1
                30      RAISE_VARARGS    ...`
- `
                        554     STORE_FAST                      20: requires_zip64
                ...`
- `
                146     MAKE_FUNCTION                   0
                148     CALL_FUNCTION    ...`
- `
                36      MAKE_FUNCTION                   0
                38      STORE_NAME       ...`
- `
                        212     STORE_FAST                      6: field
                        21...`
- `
                        16      CALL_METHOD                     1
                        18      S...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        494     LOAD_FAST                       12: x
                        496  ...`
- `
                        532     LOAD_FAST                       12: path
                        53...`
- `t read from the ZIP file while there is an open writing handle on it. Close the writing handle befor...`
- `,)
                        274     CALL_FUNCTION_KW                2
                        276    ...`
- `
                        164     STORE_FAST                      6: field
                        16...`
- `
                76      CALL_FUNCTION                   1
                78      RAISE_VARARGS    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        36      CALL_FUNCTION                   1
                        38      R...`
- `
                        114     CALL_FUNCTION                   1
                        116     L...`
- Plus 239 more strings...

### gzip_pycdas.dis

- ` not supported in binary mode"
                60      CALL_FUNCTION                   1
           ...`
- `
                        6       CALL_METHOD                     1
                        8       L...`
- `
                126     MAKE_FUNCTION                   0
                128     CALL_FUNCTION    ...`
- `
                306     BINARY_ADD                      
                308     LOAD_CONST        ...`
- `,)
                12      CALL_FUNCTION_KW                1
                14      SETUP_WITH     ...`
- `
                38      LOAD_CONST                      7: `
- `
        148     CALL_FUNCTION                   2
        150     STORE_NAME                      2...`
- `
                        50      INPLACE_ADD                     
                        52      ST...`
- `
                20      LOAD_FAST                       1: mode
                22      BUILD_TUPLE...`
- `
                        34      CALL_FUNCTION                   2
                        36      R...`
- `
                        42      BINARY_ADD                      
                        44      RE...`
- `
                166     MAKE_FUNCTION                   0
                168     STORE_NAME       ...`
- `,)
                        24      CALL_FUNCTION_KW                3
                        26     ...`
- `
                24      MAKE_FUNCTION                   0
                26      STORE_NAME       ...`
- `
        234     MAKE_FUNCTION                   0
        236     STORE_NAME                      3...`
- `
                78      MAKE_FUNCTION                   8
                80      STORE_NAME       ...`
- `
        178     LOAD_NAME                       8: _compression
        180     LOAD_ATTR          ...`
- `
                        6       LOAD_FAST                       2: mode
                        8  ...`
- `
                        250     BINARY_ADD                      
                        252     CA...`
- `
                90      BUILD_LIST                      1
                92      LOAD_CONST       ...`
- Plus 77 more strings...

### _compat_pickle_pycdas.dis

- `
        94      LOAD_CONST                      31: `
- `
        150     LOAD_CONST                      49: `
- `)
        252     MAP_ADD                         1
        254     LOAD_CONST                      ...`
- `
        212     LOAD_CONST                      69: `
- `)
        330     MAP_ADD                         1
        332     LOAD_CONST                      ...`
- `)
        380     MAP_ADD                         1
        382     LOAD_CONST                      ...`
- `)
        398     MAP_ADD                         1
        400     LOAD_CONST                      ...`
- `
        656     LOAD_CONST                      155: (`
- `)
        368     MAP_ADD                         1
        370     LOAD_CONST                      ...`
- `)
        392     MAP_ADD                         1
        394     LOAD_CONST                      ...`
- `
        220     LOAD_CONST                      73: `
- `)
        718     LOAD_CONST                      165: (`
- `
        28      LOAD_CONST                      9: `
- `
        198     LOAD_CONST                      65: `
- `)
        730     LOAD_CONST                      171: (`
- `)
        374     MAP_ADD                         1
        376     LOAD_CONST                      ...`
- `
        34      LOAD_CONST                      11: `
- `)
        696     LOAD_CONST                      160: (`
- `))
        700     BUILD_CONST_KEY_MAP             4
        702     CALL_METHOD                    ...`
- `
        180     LOAD_CONST                      59: `
- Plus 79 more strings...

### threading_pycdas.dis

- `
                18      MAKE_FUNCTION                   1
                20      STORE_NAME       ...`
- `
                66      MAKE_FUNCTION                   0
                68      STORE_NAME       ...`
- `
                        12      CALL_FUNCTION                   1
                        14      R...`
- `
        596     LOAD_NAME                       65: Thread
        598     CALL_FUNCTION           ...`
- `
        628     LOAD_NAME                       65: Thread
        630     CALL_FUNCTION           ...`
- `
                        30      STORE_FAST                      1: status
                        3...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        16      CALL_FUNCTION                   1
                        18      R...`
- `
                72      MAKE_FUNCTION                   0
                74      STORE_NAME       ...`
- `
                        58      LOAD_FAST                       0: self
                        60 ...`
- `
                48      MAKE_FUNCTION                   0
                50      STORE_NAME       ...`
- `
                66      MAKE_FUNCTION                   1
                68      STORE_NAME       ...`
- `)
                120     CALL_FUNCTION_KW                3
                122     POP_TOP         ...`
- `
        728     MAKE_FUNCTION                   0
        730     STORE_NAME                      9...`
- `
                        10      CALL_FUNCTION                   1
                        12      R...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                70      MAKE_FUNCTION                   0
                72      STORE_NAME       ...`
- `
                38      MAKE_FUNCTION                   1
                40      STORE_NAME       ...`
- `
        556     MAKE_FUNCTION                   0
        558     STORE_NAME                      6...`
- `
                56      MAKE_FUNCTION                   0
                58      STORE_NAME       ...`
- Plus 97 more strings...

### hashlib_pycdas.dis

- `
                290     STORE_SUBSCR                    
                292     LOAD_FAST         ...`
- `
        214     MAKE_FUNCTION                   0
        216     LOAD_NAME                       2...`
- `
                24      LOAD_FAST                       0: name
                26      BINARY_ADD ...`
- `,)
        252     IMPORT_NAME                     12: _hashlib
        254     IMPORT_FROM         ...`
- `)
        28      BINARY_ADD                      
        30      STORE_NAME                      5...`
- `
                198     STORE_SUBSCR                    
                200     LOAD_FAST         ...`
- `})
                32      CONTAINS_OP                     0 (in)
                34      POP_JUMP_I...`
- `
                200     MAKE_FUNCTION                   1
                202     STORE_FAST       ...`
- `
                60      STORE_SUBSCR                    
                62      JUMP_FORWARD      ...`
- `
                106     LOAD_CONST                      5: 64
                108     CALL_FUNCTION...`
- `
        66      MAKE_FUNCTION                   1
        68      STORE_NAME                      1...`
- `})
                104     CONTAINS_OP                     0 (in)
                106     POP_JUMP_I...`
- `
                288     CALL_METHOD                     2
                290     BINARY_ADD       ...`
- `
                4       LOAD_GLOBAL                     1: DeprecationWarning
                6    ...`
- `
        40      BUILD_SET                       2
        42      STORE_NAME                      7...`
- `
                338     STORE_SUBSCR                    
                340     POP_BLOCK         ...`
- `
                132     STORE_SUBSCR                    
                134     LOAD_FAST         ...`
- `
                270     STORE_SUBSCR                    
                272     LOAD_FAST         ...`
- `
        56      MAKE_FUNCTION                   0
        58      STORE_NAME                      9...`
- `
                242     STORE_SUBSCR                    
                244     JUMP_FORWARD      ...`
- Plus 9 more strings...

### fractions_pycdas.dis

- `,)
                        14      CALL_FUNCTION_KW                3
                        16     ...`
- `
                54      MAKE_FUNCTION                   0
                56      CALL_FUNCTION    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `,)
                        132     CALL_FUNCTION_KW                3
                        134    ...`
- `
                178     MAKE_FUNCTION                   0
                180     STORE_NAME       ...`
- `
                114     MAKE_FUNCTION                   0
                116     STORE_NAME       ...`
- `
                320     MAKE_FUNCTION                   0
                322     STORE_NAME       ...`
- `
                        172     CALL_FUNCTION                   1
                        174     S...`
- `
                        22      LOAD_FAST                       0: self
                        24 ...`
- `
                        448     LOAD_FAST                       1: numerator
                      ...`
- `
                304     MAKE_FUNCTION                   0
                306     STORE_NAME       ...`
- `
                352     MAKE_FUNCTION                   0
                354     STORE_NAME       ...`
- `
                402     MAKE_FUNCTION                   0
                404     STORE_NAME       ...`
- `
                450     MAKE_FUNCTION                   0
                452     STORE_NAME       ...`
- `
                        34      LOAD_FAST                       0: cls
                        36  ...`
- `
                370     MAKE_FUNCTION                   0
                372     STORE_NAME       ...`
- `
                        54      LOAD_DEREF                      0: fallback_operator
              ...`
- `
                130     MAKE_FUNCTION                   0
                132     STORE_NAME       ...`
- `
                418     MAKE_FUNCTION                   0
                420     STORE_NAME       ...`
- `,)
        8       IMPORT_NAME                     1: decimal
        10      IMPORT_FROM           ...`
- Plus 28 more strings...

### getopt_pycdas.dis

- `
                136     CALL_METHOD                     1
                138     STORE_FAST       ...`
- ` attribute, which is the\noption involved with the exception.\n"
        2       STORE_NAME         ...`
- `
                22      MAKE_FUNCTION                   1
                24      STORE_NAME       ...`
- `
                154     CALL_FUNCTION                   1
                156     LOAD_FAST        ...`
- `
                218     COMPARE_OP                      3 (!=)
                220     POP_JUMP_IF_...`
- `
                14      CALL_FUNCTION                   1
                16      COMPARE_OP       ...`
- `
                34      COMPARE_OP                      3 (!=)
                36      POP_JUMP_IF_...`
- `
                4       COMPARE_OP                      3 (!=)
                6       POP_JUMP_IF_...`
- `
                8       MAKE_FUNCTION                   8
                10      LOAD_FAST        ...`
- `
                40      CALL_METHOD                     1
                42      POP_JUMP_IF_FALSE...`
- `
                202     COMPARE_OP                      2 (==)
                204     POP_JUMP_IF_...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `,)
        26      IMPORT_NAME                     3: gettext
        28      IMPORT_FROM           ...`
- `
                14      STORE_NAME                      4: msg
                16      LOAD_CONST  ...`
- `
                60      BINARY_ADD                      
                62      LOAD_FAST         ...`
- `
        92      MAKE_FUNCTION                   1
        94      STORE_NAME                      9...`
- `
        70      MAKE_FUNCTION                   0
        72      LOAD_CONST                      8...`
- `
                58      CALL_FUNCTION                   1
                60      LOAD_FAST        ...`
- `
                130     COMPARE_OP                      3 (!=)
                132     POP_JUMP_IF_...`
- `
        176     LOAD_CONST                      25: `
- Plus 10 more strings...

### textwrap_pycdas.dis

- `
                        40      MAKE_FUNCTION                   0
                        42      L...`
- `
        22      STORE_NAME                      3: _whitespace
        24      LOAD_BUILD_CLASS    ...`
- `)
                100     BUILD_CONST_KEY_MAP             4
                102     BINARY_MODULO   ...`
- `
                10      LOAD_FAST                       0: text
                12      CALL_METHOD...`
- `
                242     MAKE_FUNCTION                   0
                244     STORE_NAME       ...`
- `
        54      MAKE_FUNCTION                   1
        56      STORE_NAME                      6...`
- `
                        40      COMPARE_OP                      2 (==)
                        42  ...`
- `
                        170     COMPARE_OP                      2 (==)
                        172 ...`
- `
        98      MAKE_FUNCTION                   0
        100     STORE_NAME                      1...`
- `)
                10      BUILD_CONST_KEY_MAP             2
                12      LOAD_FAST       ...`
- `
                34      LOAD_METHOD                     0: join
                36      LOAD_FAST  ...`
- `
                        64      LOAD_CONST                      4: 0
                        66    ...`
- `
        116     COMPARE_OP                      2 (==)
        118     POP_JUMP_IF_FALSE           ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       LOAD_FAST                       1: width
                8       BUILD_MAP ...`
- `
                20      CALL_FUNCTION                   1
                22      STORE_NAME       ...`
- `
                226     MAKE_FUNCTION                   0
                228     STORE_NAME       ...`
- `
                210     MAKE_FUNCTION                   0
                212     STORE_NAME       ...`
- `
                                12      COMPARE_OP                      3 (!=)
                    ...`
- `
                194     MAKE_FUNCTION                   0
                196     STORE_NAME       ...`
- Plus 14 more strings...

### parse_pycdas.dis

- `
        922     MAKE_FUNCTION                   0
        924     STORE_NAME                      9...`
- `
        470     MAKE_FUNCTION                   0
        472     LOAD_CONST                      3...`
- `)
                256     CALL_FUNCTION_KW                3
                258     STORE_FAST      ...`
- `
                        14      MAKE_FUNCTION                   8
                        16      L...`
- `
                66      STORE_FAST                      2: errors
                68      LOAD_GLOB...`
- `
                        12      BINARY_ADD                      
                        14      LO...`
- `, True)
        642     LOAD_CONST                      79: <CODE> urlsplit
        644     LOAD_CON...`
- `
                6       CALL_METHOD                     1
                8       POP_JUMP_IF_FALSE...`
- `
                        20      LOAD_METHOD                     2: format
                        2...`
- `
                30      LOAD_CONST                      3: `
- `
                336     LOAD_FAST                       0: url
                338     CONTAINS_OP ...`
- `
                58      BINARY_ADD                      
                60      CALL_FUNCTION     ...`
- `
        388     LOAD_NAME                       35: _ParseResultBase
        390     STORE_ATTR    ...`
- `
                42      LOAD_CONST                      3: `
- `
        628     MAKE_FUNCTION                   0
        630     STORE_NAME                      5...`
- `
                42      CALL_FUNCTION                   1
                44      RAISE_VARARGS    ...`
- `
                78      LOAD_FAST                       2: n
                80      CALL_METHOD   ...`
- `
        294     CALL_FUNCTION                   2
        296     STORE_NAME                      3...`
- `
                242     CALL_METHOD                     1
                244     STORE_FAST       ...`
- `
                6       CALL_METHOD                     1
                8       UNPACK_SEQUENCE  ...`
- Plus 147 more strings...

### ttk_pycdas.dis

- `
                        52      LOAD_FAST                       2: kw
                        54   ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        102     MAKE_FUNCTION                   0
        104     STORE_NAME                      1...`
- `,)
                48      CALL_FUNCTION_KW                3
                50      RETURN_VALUE   ...`
- `
                102     CALL_METHOD                     1
                104     POP_JUMP_IF_TRUE ...`
- `
                        12      LOAD_FAST                       1: item
                        14 ...`
- `
                        34      BINARY_SUBSCR                   
                        36      CA...`
- `
                20      CALL_METHOD                     1
                22      STORE_FAST       ...`
- `
                88      BINARY_SUBSCR                   
                90      LOAD_CONST        ...`
- `
        84      MAKE_FUNCTION                   1
        86      STORE_NAME                      1...`
- `
                        6       LOAD_FAST                       1: x
                        8     ...`
- `
                152     LOAD_FAST                       1: indent
                154     BINARY_MU...`
- `
                186     BINARY_SUBSCR                   
                188     STORE_FAST        ...`
- `
                86      MAKE_FUNCTION                   1
                88      STORE_NAME       ...`
- `
                86      MAKE_FUNCTION                   0
                88      STORE_NAME       ...`
- `
                        130     STORE_FAST                      6: scale_side
                     ...`
- `
                18      MAKE_FUNCTION                   1
                20      STORE_NAME       ...`
- `,)
                        214     CALL_FUNCTION_KW                1
                        216    ...`
- `
                        12      LOAD_FAST                       1: interval
                       ...`
- `
                70      MAKE_FUNCTION                   0
                72      STORE_NAME       ...`
- Plus 188 more strings...

### constants_pycdas.dis

- `
        74      STORE_NAME                      18: NONE
        76      LOAD_CONST                ...`
- `
        154     STORE_NAME                      38: INSIDE
        156     LOAD_CONST              ...`
- `
        82      STORE_NAME                      20: Y
        84      LOAD_CONST                   ...`
- `
        34      STORE_NAME                      8: W
        36      LOAD_CONST                    ...`
- `
        58      STORE_NAME                      14: NS
        60      LOAD_CONST                  ...`
- `
        138     STORE_NAME                      34: NUMERIC
        140     LOAD_CONST             ...`
- `
        146     STORE_NAME                      36: WORD
        148     LOAD_CONST                ...`
- `
        50      STORE_NAME                      12: NE
        52      LOAD_CONST                  ...`
- `
        98      STORE_NAME                      24: RIGHT
        100     LOAD_CONST               ...`
- `
        226     STORE_NAME                      56: SEPARATOR
        228     LOAD_CONST           ...`
- `
        130     STORE_NAME                      32: HORIZONTAL
        132     LOAD_CONST          ...`
- `
        290     STORE_NAME                      72: MITER
        292     LOAD_CONST               ...`
- `
        42      STORE_NAME                      10: NW
        44      LOAD_CONST                  ...`
- `
        210     STORE_NAME                      52: CASCADE
        212     LOAD_CONST             ...`
- `
        218     STORE_NAME                      54: COMMAND
        220     LOAD_CONST             ...`
- `
        274     STORE_NAME                      68: BUTT
        276     LOAD_CONST                ...`
- `
        194     STORE_NAME                      48: NORMAL
        196     LOAD_CONST              ...`
- `
        26      STORE_NAME                      6: N
        28      LOAD_CONST                    ...`
- `
        170     STORE_NAME                      42: SEL_LAST
        172     LOAD_CONST            ...`
- `
        282     STORE_NAME                      70: ROUND
        284     LOAD_CONST               ...`
- Plus 16 more strings...

### __init___pycdas.dis

- `
                132     COMPARE_OP                      2 (==)
                134     POP_JUMP_IF_...`
- `
                582     CALL_FUNCTION                   1
                584     RAISE_VARARGS    ...`
- `
                662     LOAD_FAST                       0: fp
                664     LOAD_ATTR    ...`
- `
        188     CALL_METHOD                     1
        190     STORE_NAME                      2...`
- `
                14      CALL_FUNCTION                   1
                16      RAISE_VARARGS    ...`
- `
        152     MAKE_FUNCTION                   0
        154     STORE_NAME                      2...`
- `
        298     MAKE_FUNCTION                   0
        300     STORE_NAME                      3...`
- `
                14      LOAD_GLOBAL                     3: type
                16      LOAD_FAST  ...`
- `,)
                308     CALL_FUNCTION_KW                2
                310     LOAD_FAST      ...`
- `
        398     LOAD_NAME                       43: BASE_INT
        400     CALL_FUNCTION         ...`
- `
                32      CALL_FUNCTION                   1
                34      RAISE_VARARGS    ...`
- `
                402     CALL_METHOD                     1
                404     STORE_FAST       ...`
- `
                592     CALL_METHOD                     1
                594     LOAD_CONST       ...`
- `,)
        52      IMPORT_NAME                     8: io
        54      IMPORT_FROM                ...`
- `
                28      LOAD_GLOBAL                     3: struct
                30      LOAD_METH...`
- `
        258     MAKE_FUNCTION                   0
        260     STORE_NAME                      3...`
- `
        458     STORE_NAME                      57: BIN_INT64
        460     LOAD_CONST           ...`
- `
        434     STORE_NAME                      51: BIN_FLOAT32
        436     LOAD_CONST         ...`
- `
        426     STORE_NAME                      49: BIN_STRING
        428     LOAD_CONST          ...`
- `
                232     LOAD_GLOBAL                     12: getattr
                234     LOAD_FA...`
- Plus 72 more strings...

### scanner_pycdas.dis

- `
                        352     COMPARE_OP                      2 (==)
                        354 ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
        54      BUILD_LIST                      1
        56      STORE_NAME                      6...`
- `
                        440     COMPARE_OP                      2 (==)
                        442 ...`
- `
                        186     COMPARE_OP                      2 (==)
                        188 ...`
- `
                        376     COMPARE_OP                      2 (==)
                        378 ...`
- `py_make_scanner`
- `
                        100     COMPARE_OP                      2 (==)
                        102 ...`
- `
                        42      COMPARE_OP                      2 (==)
                        44  ...`
- `
                        146     COMPARE_OP                      2 (==)
                        148 ...`
- `
                96      MAKE_FUNCTION                   8
                98      STORE_DEREF      ...`
- `
                        404     CALL_FUNCTION                   1
                        406     L...`
- `
                        300     BINARY_ADD                      
                        302     CA...`
- `
                        226     COMPARE_OP                      2 (==)
                        228 ...`

### decoder_pycdas.dis

- `
                236     COMPARE_OP                      2 (==)
                238     POP_JUMP_IF_...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                40      CONTAINS_OP                     1 (not in)
                42      POP_JUMP...`
- `
        68      BUILD_LIST                      2
        70      STORE_NAME                      8...`
- `)
        138     BUILD_CONST_KEY_MAP             3
        140     STORE_NAME                      ...`
- `
                166     LOAD_FAST                       0: s
                168     LOAD_FAST     ...`
- `
        164     LOAD_CONST                      18: `
- `
        256     MAKE_FUNCTION                   1
        258     STORE_NAME                      2...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                74      COMPARE_OP                      2 (==)
                76      POP_JUMP_IF_...`
- `
                        38      LOAD_FAST                       1: msg
                        40  ...`
- `,)
        30      IMPORT_NAME                     4: _json
        32      IMPORT_FROM             ...`
- ` delimiter"
                280     LOAD_FAST                       8: s
                282     LOA...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                56      COMPARE_OP                      3 (!=)
                58      POP_JUMP_IF_...`
- `
                        46      LOAD_FAST                       1: s
                        48    ...`
- `
        160     LOAD_CONST                      16: `
- `
        102     CALL_FUNCTION                   1
        104     STORE_NAME                      1...`
- `)
                26      BUILD_CONST_KEY_MAP             6
                28      LOAD_CONST      ...`
- `
        120     MAKE_FUNCTION                   0
        122     LOAD_CONST                      6...`
- Plus 19 more strings...

### encoder_pycdas.dis

- `
        268     LOAD_NAME                       24: object
        270     CALL_FUNCTION           ...`
- `
                52      MAKE_FUNCTION                   0
                54      STORE_NAME       ...`
- `
                        218     BINARY_ADD                      
                        220     YI...`
- `
                20      LOAD_DEREF                      4: _indent
                22      BINARY_M...`
- `
                        198     STORE_FAST                      7: key
                        200 ...`
- `
        174     LOAD_CONST                      15: `
- `
                                38      STORE_FAST                      5: text
                   ...`
- `
                        8       YIELD_VALUE                     
                        10      PO...`
- `
                120     MAKE_FUNCTION                   8
                122     STORE_DEREF      ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        8       YIELD_VALUE                     
                        10      PO...`
- `
        138     CALL_METHOD                     1
        140     STORE_NAME                      1...`
- `)
                38      BUILD_CONST_KEY_MAP             8
                40      LOAD_CONST      ...`
- `)
        178     BUILD_CONST_KEY_MAP             7
        180     STORE_NAME                      ...`
- `
                70      MAKE_FUNCTION                   1
                72      STORE_NAME       ...`
- `
                24      BINARY_ADD                      
                26      RETURN_VALUE      ...`
- `
                        338     YIELD_VALUE                     
                        340     PO...`
- `
                        58      STORE_FAST                      3: buf
                        60  ...`
- `
                                10      STORE_FAST                      5: text
                   ...`
- `,)
        58      IMPORT_NAME                     2: _json
        60      IMPORT_FROM             ...`
- Plus 21 more strings...

### readers_pycdas.dis

- `
                24      MAKE_FUNCTION                   8
                26      STORE_NAME       ...`
- `
                40      MAKE_FUNCTION                   0
                42      STORE_NAME       ...`
- `
                        2       LOAD_METHOD                     0: join
                        4  ...`
- `
                        30      STORE_FAST                      2: message
                        ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                48      MAKE_FUNCTION                   0
                50      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        68      MAKE_FUNCTION                   0
        70      LOAD_CONST                      9...`
- `
        50      MAKE_FUNCTION                   0
        52      LOAD_CONST                      7...`
- `
                        64      CALL_FUNCTION                   1
                        66      R...`
- `"
                                10      LOAD_FAST                       1: path
                  ...`
- `
                        26      CALL_METHOD                     2
                        28      L...`
- `
                        24      LOAD_FAST                       1: paths
                        26...`
- `,)
        28      IMPORT_NAME                     3: 
        30      IMPORT_FROM                  ...`
- `
                        8       BUILD_STRING                    2
                        10      C...`
- `
                        6       CALL_METHOD                     1
                        8       U...`
- `
        86      MAKE_FUNCTION                   0
        88      LOAD_CONST                      1...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                86      MAKE_FUNCTION                   0
                88      CALL_FUNCTION    ...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- Plus 4 more strings...

### util_pycdas.dis

- `
                        34      STORE_SUBSCR                    
                        36      LO...`
- `
                6       CALL_METHOD                     1
                8       POP_JUMP_IF_TRUE ...`
- `,)
        116     IMPORT_NAME                     8: _bootstrap_external
        118     IMPORT_FRO...`
- `,)
        44      IMPORT_NAME                     3: _bootstrap
        46      IMPORT_FROM        ...`
- `
                96      LOAD_FAST                       3: parent_name
                98      FORM...`
- `
        270     LOAD_NAME                       20: types
        272     LOAD_ATTR                ...`
- `
                        6       CALL_FUNCTION                   2
                        8       P...`
- `LazyLoader`
- `
        240     MAKE_FUNCTION                   0
        242     STORE_NAME                      2...`
- `
                58      BUILD_LIST                      1
                60      LOAD_CONST       ...`
- `
                32      MAKE_FUNCTION                   8
                34      CALL_FUNCTION    ...`
- `
        256     MAKE_FUNCTION                   0
        258     STORE_NAME                      2...`
- `
                16      MAKE_FUNCTION                   8
                18      CALL_FUNCTION    ...`
- `,)
                112     CALL_FUNCTION_KW                2
                114     LOAD_FAST      ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                218     LOAD_METHOD                     12: format
                220     LOAD_FAS...`
- `,)
        92      IMPORT_NAME                     8: _bootstrap_external
        94      IMPORT_FRO...`
- `
                6       CALL_METHOD                     1
                8       POP_JUMP_IF_FALSE...`
- `
                6       LOAD_GLOBAL                     2: DeprecationWarning
                8    ...`
- `
                18      MAKE_FUNCTION                   0
                20      CALL_FUNCTION    ...`
- Plus 20 more strings...

### abc_pycdas.dis

- `
                        4       MAKE_FUNCTION                   0
                        6       L...`
- `,)
        282     CALL_FUNCTION_KW                3
        284     STORE_NAME                     ...`
- `
                58      MAKE_FUNCTION                   4
                60      CALL_FUNCTION    ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `)
        182     IMPORT_NAME                     13: typing
        184     IMPORT_FROM            ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
        208     MAKE_FUNCTION                   0
        210     LOAD_CONST                      1...`
- `
        492     MAKE_FUNCTION                   0
        494     LOAD_CONST                      3...`
- `
                        6       LOAD_GLOBAL                     2: DeprecationWarning
             ...`
- `
                102     MAKE_FUNCTION                   4
                104     CALL_FUNCTION    ...`
- `,)
        134     IMPORT_NAME                     9: _abc
        136     IMPORT_FROM              ...`
- `
                18      LOAD_NAME                       6: Text
                20      LOAD_CONST ...`
- `
        456     LOAD_NAME                       11: abc
        458     LOAD_ATTR                  ...`
- `
                102     MAKE_FUNCTION                   0
                104     STORE_NAME       ...`
- `
                78      MAKE_FUNCTION                   4
                80      CALL_FUNCTION    ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                40      MAKE_FUNCTION                   1
                42      STORE_NAME       ...`
- `
                38      MAKE_FUNCTION                   0
                40      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        272     MAKE_FUNCTION                   0
        274     LOAD_CONST                      1...`
- Plus 36 more strings...

### _bootstrap_pycdas.dis

- `
                        40      LOAD_METHOD                     0: format
                        4...`
- `
                        16      LOAD_METHOD                     4: format
                        1...`
- `
        130     MAKE_FUNCTION                   0
        132     STORE_NAME                      1...`
- `
        190     CALL_FUNCTION                   2
        192     STORE_NAME                      2...`
- `,)
                100     CALL_FUNCTION_KW                4
                102     POP_TOP        ...`
- `,)
                100     CALL_FUNCTION_KW                3
                102     POP_TOP        ...`
- `
                6       LOAD_CONST                      2: None
                8       CALL_FUNCTI...`
- `
                46      CALL_FUNCTION                   1
                48      RAISE_VARARGS    ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        18      CALL_METHOD                     1
                        20      L...`
- `
                134     CALL_METHOD                     1
                136     LOAD_CONST       ...`
- `
                10      LOAD_CONST                      0: None
                12      CALL_FUNCTI...`
- `
                184     LOAD_CONST                      0: None
                186     CALL_FUNCTI...`
- `t resolve package from __spec__ or __package__, falling back on __name__ and __path__"
             ...`
- `
                78      MAKE_FUNCTION                   0
                80      CALL_FUNCTION    ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                50      LOAD_METHOD                     3: format
                52      LOAD_FAST...`
- `
                18      CALL_FUNCTION                   2
                20      POP_JUMP_IF_TRUE ...`
- `
                36      MAKE_FUNCTION                   1
                38      CALL_FUNCTION    ...`
- `
                120     MAKE_FUNCTION                   0
                122     CALL_FUNCTION    ...`
- Plus 108 more strings...

### _abc_pycdas.dis

- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        6       CALL_FUNCTION                   2
                        8       P...`
- `metaclass`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
        38      MAKE_FUNCTION                   0
        40      LOAD_CONST                      6...`
- `
                        6       LOAD_GLOBAL                     2: DeprecationWarning
             ...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`

### _bootstrap_external_pycdas.dis

- `
                276     COMPARE_OP                      2 (==)
                278     POP_JUMP_IF_...`
- `
                14      STORE_NAME                      4: REGISTRY_KEY
                16      LOA...`
- `
        212     MAKE_FUNCTION                   0
        214     STORE_NAME                      2...`
- `
        94      LOAD_CONST                      5: `
- `
                42      MAKE_FUNCTION                   0
                44      CALL_FUNCTION    ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                58      MAKE_FUNCTION                   0
                60      CALL_FUNCTION    ...`
- `
                50      MAKE_FUNCTION                   0
                52      CALL_FUNCTION    ...`
- `
                66      MAKE_FUNCTION                   0
                68      STORE_NAME       ...`
- `
                        24      LOAD_METHOD                     3: format
                        2...`
- `
                6       CALL_METHOD                     1
                8       STORE_FAST       ...`
- `
        610     CALL_FUNCTION                   2
        612     STORE_NAME                      7...`
- `,)
                32      BUILD_CONST_KEY_MAP             1
                34      LOAD_CONST     ...`
- `
                100     STORE_SUBSCR                    
                102     LOAD_FAST         ...`
- `
        528     MAKE_FUNCTION                   0
        530     STORE_NAME                      6...`
- `
                36      MAKE_FUNCTION                   0
                38      STORE_NAME       ...`
- `
        148     LOAD_METHOD                     18: join
        150     LOAD_NAME                 ...`
- `,)
                52      BUILD_CONST_KEY_MAP             1
                54      LOAD_CONST     ...`
- `
                16      CALL_FUNCTION                   1
                18      RAISE_VARARGS    ...`
- `
                        6       LOAD_FAST                       0: self
                        8  ...`
- Plus 157 more strings...

### machinery_pycdas.dis

- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `,)
        132     IMPORT_NAME                     5: _bootstrap_external
        134     IMPORT_FRO...`
- `,)
        84      IMPORT_NAME                     5: _bootstrap_external
        86      IMPORT_FRO...`
- `)
        44      IMPORT_NAME                     5: _bootstrap_external
        46      IMPORT_FROM...`
- `,)
        108     IMPORT_NAME                     5: _bootstrap_external
        110     IMPORT_FRO...`
- `,)
        20      IMPORT_NAME                     1: _bootstrap
        22      IMPORT_FROM        ...`

### _collections_pycdas.dis

- `
                        6       LOAD_GLOBAL                     1: super
                        8 ...`
- `
                20      MAKE_FUNCTION                   8
                22      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        32      MAKE_FUNCTION                   0
        34      LOAD_CONST                      5...`
- `
        42      LOAD_CONST                      6: `
- `
                        8       MAKE_FUNCTION                   8
                        10      L...`
- `
                        14      LOAD_CONST                      2: 1
                        16    ...`
- `
        14      MAKE_FUNCTION                   0
        16      LOAD_CONST                      3...`

### _meta_pycdas.dis

- `
        50      MAKE_FUNCTION                   0
        52      LOAD_CONST                      4...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                18      MAKE_FUNCTION                   4
                20      STORE_NAME       ...`
- `
                42      LOAD_NAME                       5: str
                44      LOAD_CONST  ...`
- `
                54      MAKE_FUNCTION                   4
                56      STORE_NAME       ...`
- `
                72      MAKE_FUNCTION                   4
                74      STORE_NAME       ...`
- `
                108     MAKE_FUNCTION                   5
                110     STORE_NAME       ...`
- `
                144     MAKE_FUNCTION                   4
                146     CALL_FUNCTION    ...`
- `
                84      LOAD_NAME                       11: _T
                86      LOAD_CONST  ...`
- `)
                24      LOAD_CONST                      5: <CODE> __div__
                26      ...`
- `
        66      MAKE_FUNCTION                   0
        68      LOAD_CONST                      6...`
- `)
        4       IMPORT_NAME                     0: typing
        6       IMPORT_FROM             ...`
- `)
                34      LOAD_CONST                      7: <CODE> parent
                36      L...`
- `
                44      LOAD_NAME                       7: str
                46      BUILD_TUPLE ...`
- `
                28      LOAD_NAME                       6: bool
                30      BUILD_TUPLE...`
- `)
                14      LOAD_CONST                      3: <CODE> joinpath
                16     ...`

### _functools_pycdas.dis

- `
        22      MAKE_FUNCTION                   1
        24      STORE_NAME                      2...`
- `
                16      MAKE_FUNCTION                   8
                18      CALL_FUNCTION    ...`
- `
                22      MAKE_FUNCTION                   8
                24      STORE_FAST       ...`

### _adapters_pycdas.dis

- `
                        4       MAKE_FUNCTION                   0
                        6       S...`
- `
                74      MAKE_FUNCTION                   0
                76      STORE_NAME       ...`
- `
                                6       LOAD_FAST                       0: value
                  ...`
- `
                30      LOAD_NAME                       7: email
                32      LOAD_ATTR ...`
- `,)
        28      IMPORT_NAME                     4: _text
        30      IMPORT_FROM             ...`
- `
                        8       MAKE_FUNCTION                   8
                        10      S...`
- `
                                32      COMPARE_OP                      2 (==)
                    ...`
- `
                        26      BINARY_SUBSCR                   
                        28      GE...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                                58      LOAD_CONST                      4: `
- `Message`
- `
                54      MAKE_FUNCTION                   0
                56      STORE_NAME       ...`

### _text_pycdas.dis

- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `FoldedCase`
- `
                102     MAKE_FUNCTION                   1
                104     STORE_NAME       ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                92      MAKE_FUNCTION                   0
                94      STORE_NAME       ...`
- `,)
        12      IMPORT_NAME                     1: _functools
        14      IMPORT_FROM        ...`
- `
                68      MAKE_FUNCTION                   0
                70      STORE_NAME       ...`
- `
                32      MAKE_FUNCTION                   0
                34      STORE_NAME       ...`
- `
                48      MAKE_FUNCTION                   0
                50      STORE_NAME       ...`

### policy_pycdas.dis

- `
                22      STORE_NAME                      7: refold_source
                24      LO...`
- `
        118     MAKE_FUNCTION                   0
        120     LOAD_CONST                      1...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `)
        174     CALL_FUNCTION_KW                2
        176     STORE_NAME                      ...`
- `
                        30      JUMP_FORWARD                    1 (to 34)
                        3...`
- `
                82      MAKE_FUNCTION                   0
                84      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `,)
        148     CALL_FUNCTION_KW                1
        150     STORE_NAME                     ...`
- `,)
                        168     CALL_FUNCTION_KW                1
                        170    ...`
- `
                        14      COMPARE_OP                      2 (==)
                        16  ...`
- `
                66      MAKE_FUNCTION                   0
                68      STORE_NAME       ...`
- `
                        30      LOAD_METHOD                     2: join
                        32 ...`
- `
                50      MAKE_FUNCTION                   0
                52      STORE_NAME       ...`
- `
                        6       CALL_FUNCTION                   2
                        8       P...`
- `,)
        160     CALL_FUNCTION_KW                1
        162     STORE_NAME                     ...`
- `
                        6       CALL_FUNCTION                   2
                        8       P...`
- `
                        10      LOAD_CONST                      3: 1
                        12    ...`
- `)
        96      LIST_EXTEND                     1
        98      STORE_NAME                      ...`
- `
                100     MAKE_FUNCTION                   1
                102     STORE_NAME       ...`
- `
                        44      CALL_METHOD                     2
                        46      R...`
- Plus 7 more strings...

### header_pycdas.dis

- `)
                        12      CONTAINS_OP                     0 (in)
                        14 ...`
- `
                        66      LOAD_CONST                      4: `
- `)
                        108     CONTAINS_OP                     1 (not in)
                       ...`
- `
        84      STORE_NAME                      14: BSPACE
        86      LOAD_CONST              ...`
- `
                        6       LOAD_GLOBAL                     2: FWS
                        8   ...`
- `
                        72      CALL_METHOD                     2
                        74      S...`
- `
                        218     LOAD_CONST                      7: `
- `
                46      MAKE_FUNCTION                   1
                48      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       NOP...`
- `
                68      MAKE_FUNCTION                   0
                70      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                482     LOAD_FAST                       7: encoding
                484     BINARY_...`
- `
        222     MAKE_FUNCTION                   0
        224     LOAD_CONST                      2...`
- `
                        8       LOAD_CONST                      2: `
- `
        154     CALL_METHOD                     1
        156     STORE_NAME                      2...`
- `
        208     MAKE_FUNCTION                   0
        210     LOAD_CONST                      2...`
- `)
                        14      RETURN_VALUE                    
                        16      L...`
- `
                26      MAKE_FUNCTION                   0
                28      STORE_NAME       ...`
- `
        106     CALL_FUNCTION                   1
        108     STORE_NAME                      1...`
- `
        124     LOAD_NAME                       2: re
        126     LOAD_ATTR                    ...`
- Plus 33 more strings...

### utils_pycdas.dis

- `
                6       LOAD_CONST                      2: `
- `
                74      CALL_METHOD                     2
                76      UNPACK_SEQUENCE  ...`
- `,)
                256     CALL_FUNCTION_KW                1
                258     RETURN_VALUE   ...`
- `,)
        128     IMPORT_NAME                     18: email.charset
        130     IMPORT_FROM    ...`
- `,)
        72      IMPORT_NAME                     10: email._parseaddr
        74      IMPORT_FROM ...`
- `
                212     LOAD_CONST                      10: (`
- `
        342     MAKE_FUNCTION                   1
        344     STORE_NAME                      4...`
- `
                80      LOAD_FAST                       4: encoded_name
                82      LOA...`
- `
                32      COMPARE_OP                      2 (==)
                34      POP_JUMP_IF_...`
- `)"
                22      STORE_FAST                      2: v
                24      LOAD_FAST   ...`
- `
        180     MAKE_FUNCTION                   0
        182     STORE_NAME                      2...`
- `)
                108     RETURN_VALUE                    
                110     LOAD_FAST        ...`
- `
                134     LOAD_METHOD                     3: join
                136     LOAD_FAST  ...`
- `
                34      LOAD_FAST                       3: ch
                36      BINARY_ADD   ...`
- `
                2       BUILD_LIST                      0
                4       LOAD_CONST       ...`
- `
                18      LOAD_CONST                      3: `
- `)
                18      CALL_FUNCTION_KW                3
                20      STORE_FAST      ...`
- `
                58      CALL_FUNCTION                   2
                60      STORE_FAST       ...`
- `,)
                100     CALL_FUNCTION_KW                1
                102     STORE_FAST     ...`
- `
        364     MAKE_FUNCTION                   0
        366     STORE_NAME                      4...`
- Plus 39 more strings...

### _policybase_pycdas.dis

- `
                        28      LOAD_CONST                      4: `
- `
                        10      LOAD_FAST                       1: name
                        12 ...`
- `
        2       STORE_NAME                      0: __doc__
        4       LOAD_CONST              ...`
- `
                        50      LOAD_METHOD                     6: format
                        5...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                60      MAKE_FUNCTION                   0
                62      STORE_NAME       ...`
- `
                        4       MAKE_FUNCTION                   0
                        6       L...`
- `,)
        28      IMPORT_NAME                     2: email
        30      IMPORT_FROM             ...`
- `)
                        36      CALL_FUNCTION_KW                3
                        38      ...`
- `
                36      BINARY_ADD                      
                38      LOAD_FAST         ...`
- `
        96      LOAD_NAME                       9: _PolicyBase
        98      LOAD_NAME           ...`
- `
                52      MAKE_FUNCTION                   0
                54      STORE_NAME       ...`
- `,)
                        86      CALL_FUNCTION_KW                2
                        88     ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        14      COMPARE_OP                      2 (==)
                        16  ...`
- `
                20      MAKE_FUNCTION                   0
                22      STORE_NAME       ...`
- `
                14      CALL_METHOD                     1
                16      POP_JUMP_IF_FALSE...`
- `
                        30      LOAD_METHOD                     2: join
                        32 ...`
- `
                36      MAKE_FUNCTION                   0
                38      STORE_NAME       ...`
- `
                        78      LOAD_METHOD                     8: format
                        8...`
- Plus 20 more strings...

### _parseaddr_pycdas.dis

- `
                6       LOAD_CONST                      2: `
- `
        140     CALL_FUNCTION                   2
        142     STORE_NAME                      1...`
- `
                        2       BUILD_LIST                      1
                        4       S...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
        38      STORE_NAME                      6: COMMASPACE
        40      BUILD_LIST           ...`
- `
                        96      COMPARE_OP                      2 (==)
                        98  ...`
- `
                        2       LOAD_FAST                       0: self
                        4  ...`
- `
                        102     CONTAINS_OP                     0 (in)
                        104 ...`
- `
                        44      COMPARE_OP                      2 (==)
                        46  ...`
- `
                        174     COMPARE_OP                      2 (==)
                        176 ...`
- `
                530     CALL_METHOD                     1
                532     STORE_FAST       ...`
- `
                        2       LOAD_FAST                       0: self
                        4  ...`
- `)
        52      LIST_EXTEND                     1
        54      STORE_NAME                      ...`
- `
                452     COMPARE_OP                      2 (==)
                454     POP_JUMP_IF_...`
- `
                        136     COMPARE_OP                      2 (==)
                        138 ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
                        168     COMPARE_OP                      2 (==)
                        170 ...`
- `)
                        48      CALL_METHOD                     1
                        50      ...`
- `
                        18      RETURN_VALUE                    
                        20      LO...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- Plus 37 more strings...

### encoders_pycdas.dis

- `
        2       STORE_NAME                      0: __doc__
        4       BUILD_LIST              ...`
- `
        40      MAKE_FUNCTION                   0
        42      STORE_NAME                      8...`
- `
                26      STORE_SUBSCR                    
                28      LOAD_CONST        ...`
- `,)
                8       CALL_FUNCTION_KW                1
                10      STORE_FAST     ...`
- `
                36      STORE_SUBSCR                    
                38      LOAD_CONST        ...`
- `,)
                8       CALL_FUNCTION_KW                1
                10      STORE_FAST     ...`
- `
                78      LOAD_FAST                       0: msg
                80      LOAD_CONST  ...`
- `
                38      LOAD_FAST                       0: msg
                40      LOAD_CONST  ...`
- `
        56      MAKE_FUNCTION                   0
        58      STORE_NAME                      1...`
- `,)
                8       CALL_FUNCTION_KW                1
                10      STORE_FAST     ...`
- `encode_noop`
- `,)
                8       CALL_FUNCTION_KW                2
                10      STORE_FAST     ...`
- `
                20      CALL_METHOD                     2
                22      RETURN_VALUE     ...`
- `,)
        16      IMPORT_NAME                     2: base64
        18      IMPORT_FROM            ...`
- `
                62      LOAD_FAST                       0: msg
                64      LOAD_CONST  ...`

### headerregistry_pycdas.dis

- `
                        34      BINARY_SUBSCR                   
                        36      LO...`
- `
                        2       LOAD_METHOD                     0: join
                        4  ...`
- `
        140     MAKE_FUNCTION                   0
        142     LOAD_CONST                      1...`
- `
        438     MAKE_FUNCTION                   0
        440     LOAD_CONST                      6...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                                34      CALL_FUNCTION                   3
                         ...`
- `
                24      MAKE_FUNCTION                   0
                26      CALL_FUNCTION    ...`
- `
                54      MAKE_FUNCTION                   0
                56      CALL_FUNCTION    ...`
- `
                46      MAKE_FUNCTION                   0
                48      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        32      LOAD_FAST                       2: kwds
                        34 ...`
- `
                        2       LOAD_METHOD                     0: format
                        4...`
- `
                        18      LOAD_METHOD                     3: format
                        2...`
- `
                        2       BUILD_LIST                      0
                        4       B...`
- `
                        14      STORE_SUBSCR                    
                        16      ST...`
- `
                        8       CALL_METHOD                     1
                        10      C...`
- `
                62      MAKE_FUNCTION                   0
                64      STORE_NAME       ...`
- `
        366     LOAD_NAME                       18: UniqueAddressHeader
        368     MAP_ADD    ...`
- Plus 102 more strings...

### message_pycdas.dis

- `
                        66      LOAD_CONST                      4: `
- `
                        14      CALL_METHOD                     1
                        16      L...`
- `
                128     LOAD_FAST                       0: param
                130     LOAD_FAST ...`
- `
                108     MAKE_FUNCTION                   1
                110     STORE_NAME       ...`
- `
                        6       CALL_FUNCTION                   2
                        8       P...`
- `
                        204     LOAD_FAST                       3: boundary
                       ...`
- `
                        134     CALL_METHOD                     1
                        136     L...`
- `
                        74      LOAD_CONST                      5: `
- `,)
        56      IMPORT_NAME                     8: email
        58      IMPORT_FROM             ...`
- `
                        12      LOAD_FAST                       1: missing
                        ...`
- `
                222     MAKE_FUNCTION                   0
                224     STORE_NAME       ...`
- `
        150     MAKE_FUNCTION                   1
        152     STORE_NAME                      2...`
- `,)
                        52      CALL_FUNCTION_KW                1
                        54     ...`
- `
                        40      COMPARE_OP                      2 (==)
                        42  ...`
- `
                        264     LOAD_FAST                       2: cte
                        266 ...`
- `
                        180     COMPARE_OP                      2 (==)
                        182 ...`
- `
                156     MAKE_FUNCTION                   1
                158     STORE_NAME       ...`
- `
                        6       LOAD_CONST                      2: (`
- `
                        64      LOAD_GLOBAL                     5: type
                        66 ...`
- `,)
                        4       IMPORT_NAME                     0: email.generator
              ...`
- Plus 126 more strings...

### quoprimime_pycdas.dis

- `
                6       LOAD_CONST                      2: `
- `
        46      STORE_NAME                      8: NL
        48      LOAD_CONST                   ...`
- `
        102     CALL_METHOD                     1
        104     BINARY_ADD                      
...`
- `
        310     MAKE_FUNCTION                   0
        312     STORE_NAME                      3...`
- `
                120     COMPARE_OP                      2 (==)
                122     POP_JUMP_IF_...`
- `
                12      CALL_FUNCTION                   1
                14      RAISE_VARARGS    ...`
- `
        234     MAKE_FUNCTION                   1
        236     STORE_NAME                      2...`
- `
                368     CALL_FUNCTION                   1
                370     POP_TOP          ...`
- `
        198     MAKE_FUNCTION                   0
        200     STORE_NAME                      2...`
- `
                6       RETURN_VALUE                    
                8       LOAD_FAST         ...`
- `
                18      LOAD_GLOBAL                     3: _unquote_match
                20      L...`
- `
                10      STORE_FAST                      2: decoded
                12      LOAD_FAS...`
- `
        150     GET_ITER                        
        152     FOR_ITER                        8 ...`
- `
        182     MAKE_FUNCTION                   0
        184     STORE_NAME                      1...`
- `
                250     CONTAINS_OP                     1 (not in)
                252     POP_JUMP...`
- ` in a header.  This method is commonly used for 8-bit real names\nin To:/From:/Cc: etc. fields, as w...`
- `
        208     MAKE_FUNCTION                   1
        210     STORE_NAME                      2...`
- `
                26      LOAD_FAST                       1: charset
                28      LOAD_FAS...`
- `
                210     BINARY_ADD                      
                212     CALL_FUNCTION     ...`
- `
        282     MAKE_FUNCTION                   1
        284     STORE_NAME                      2...`
- Plus 6 more strings...

### contentmanager_pycdas.dis

- `,)
                8       CALL_FUNCTION_KW                1
                10      STORE_FAST     ...`
- `
                382     LOAD_METHOD                     15: format
                384     LOAD_FAS...`
- `
                68      COMPARE_OP                      2 (==)
                70      POP_JUMP_IF_...`
- `
                126     LOAD_METHOD                     9: format
                128     LOAD_FAST...`
- `
        124     MAKE_FUNCTION                   0
        126     STORE_NAME                      1...`
- `
                22      CALL_METHOD                     1
                24      STORE_DEREF      ...`
- `
        172     LOAD_NAME                       15: get_and_fixup_unknown_message_content
        1...`
- `
                4       COMPARE_OP                      2 (==)
                6       POP_JUMP_IF_...`
- `
                248     COMPARE_OP                      2 (==)
                250     POP_JUMP_IF_...`
- `
                        2       LOAD_METHOD                     0: join
                        4  ...`
- `
        222     MAKE_FUNCTION                   1
        224     STORE_NAME                      2...`
- `
                36      MAKE_FUNCTION                   0
                38      STORE_NAME       ...`
- `
                84      LOAD_METHOD                     1: format
                86      LOAD_FAST...`
- `
        250     MAKE_FUNCTION                   1
        252     STORE_NAME                      2...`
- `
                72      CALL_METHOD                     1
                74      STORE_FAST       ...`
- `
        54      CALL_FUNCTION                   2
        56      STORE_NAME                      6...`
- `
                        66      LOAD_METHOD                     5: join
                        68 ...`
- `
        90      MAKE_FUNCTION                   0
        92      STORE_NAME                      1...`
- `
                2       LOAD_METHOD                     0: join
                4       LOAD_FAST  ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- Plus 38 more strings...

### _encoded_words_pycdas.dis

- `
        134     CALL_FUNCTION                   1
        136     STORE_SUBSCR                    
...`
- `)
        218     LOAD_CONST                      30: <CODE> encode
        220     LOAD_CONST      ...`
- `
                2       LOAD_METHOD                     0: join
                4       LOAD_CONST ...`
- `
                16      CALL_METHOD                     2
                18      STORE_FAST       ...`
- `,)
                52      CALL_FUNCTION_KW                2
                54      LOAD_FAST      ...`
- `
                6       CALL_METHOD                     1
                8       UNPACK_SEQUENCE  ...`
- `
                150     BINARY_ADD                      
                152     LOAD_CONST        ...`
- `
                82      STORE_FAST                      2: encoding
                84      LOAD_GL...`
- `
        100     MAKE_FUNCTION                   0
        102     STORE_NAME                      1...`
- `
                36      MAKE_FUNCTION                   0
                38      STORE_NAME       ...`
- `
        114     LOAD_NAME                       16: dict
        116     CALL_FUNCTION             ...`
- `
                16      CALL_METHOD                     1
                18      BINARY_ADD       ...`
- `
                12      CALL_METHOD                     1
                14      RETURN_VALUE     ...`
- `
                190     LOAD_FAST                       2: charset
                192     FORMAT_V...`
- `
                110     LOAD_METHOD                     3: format
                112     LOAD_FAST...`
- `
                6       LOAD_CONST                      2: b`
- `
                50      LOAD_CONST                      4: `
- `,)
        56      IMPORT_NAME                     8: email
        58      IMPORT_FROM             ...`
- `
                4       COMPARE_OP                      2 (==)
                6       POP_JUMP_IF_...`
- `
                18      LOAD_CONST                      0: None
                20      LOAD_CONST ...`
- Plus 13 more strings...

### base64mime_pycdas.dis

- `,)
        16      IMPORT_NAME                     2: base64
        18      IMPORT_FROM            ...`
- `
        42      STORE_NAME                      7: CRLF
        44      LOAD_CONST                 ...`
- `
        50      STORE_NAME                      9: EMPTYSTRING
        52      LOAD_CONST          ...`
- `
        84      MAKE_FUNCTION                   1
        86      STORE_NAME                      1...`
- `
                6       RETURN_VALUE                    
                8       LOAD_GLOBAL       ...`
- ` in a header.  This method is commonly used for 8-bit real names\nin To:, From:, Cc:, etc. fields, a...`
- `
                28      CALL_METHOD                     1
                30      CALL_FUNCTION    ...`
- `
                6       RETURN_VALUE                    
                8       BUILD_LIST        ...`
- `,)
        66      LOAD_CONST                      12: <CODE> header_encode
        68      LOAD_CON...`
- `
                44      LOAD_FAST                       1: charset
                46      LOAD_FAS...`

### generator_pycdas.dis

- `)
                        54      CALL_FUNCTION_KW                3
                        56      ...`
- `
                        44      LOAD_FAST                       4: specific
                       ...`
- `
                        154     LOAD_CONST                      0: None
                        156...`
- `
                134     MAKE_FUNCTION                   0
                136     STORE_NAME       ...`
- `
        110     CALL_METHOD                     1
        112     STORE_NAME                      1...`
- `
                        14      LOAD_GLOBAL                     4: _fmt
                        16 ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
        178     MAKE_FUNCTION                   0
        180     LOAD_CONST                      1...`
- `
                        122     LOAD_FAST                       4: munge_cte
                      ...`
- `
                        86      DELETE_SUBSCR                   
                        88      LO...`
- `,)
                        44      CALL_FUNCTION_KW                2
                        46     ...`
- `
                        110     CALL_METHOD                     2
                        112     L...`
- `,)
        48      IMPORT_NAME                     6: copy
        50      IMPORT_FROM              ...`
- `,)
                        38      CALL_FUNCTION_KW                1
                        40     ...`
- `
                        10      CALL_METHOD                     1
                        12      L...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `,)
                        18      CALL_FUNCTION_KW                4
                        20     ...`
- `,)
                        14      CALL_FUNCTION_KW                1
                        16     ...`
- `)
                        48      CALL_FUNCTION_KW                3
                        50      ...`
- `
                        90      LOAD_FAST                       0: self
                        92 ...`
- Plus 39 more strings...

### parser_pycdas.dis

- `
                22      MAKE_FUNCTION                   1
                24      STORE_NAME       ...`
- `)
        16      IMPORT_NAME                     2: io
        18      IMPORT_FROM                 ...`
- `
                20      MAKE_FUNCTION                   3
                22      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        80      LOAD_NAME                       10: Parser
        82      CALL_FUNCTION           ...`
- `,)
        48      IMPORT_NAME                     8: email._policybase
        50      IMPORT_FROM ...`
- `
                24      MAKE_FUNCTION                   1
                26      STORE_NAME       ...`
- `
                        6       LOAD_CONST                      2: `
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `,)
                        14      CALL_FUNCTION_KW                2
                        16     ...`
- `,)
                        10      CALL_FUNCTION_KW                2
                        12     ...`
- `)
                        10      CALL_FUNCTION_KW                3
                        12      ...`
- `,)
                        12      CALL_FUNCTION_KW                2
                        14     ...`
- `BytesHeaderParser`
- `
                40      MAKE_FUNCTION                   1
                42      STORE_NAME       ...`
- `
                24      MAKE_FUNCTION                   1
                26      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
        2       STORE_NAME                      0: __doc__
        4       BUILD_LIST              ...`
- `
        96      CALL_FUNCTION                   2
        98      STORE_NAME                      1...`
- `,)
                        12      CALL_FUNCTION_KW                3
                        14     ...`
- Plus 1 more strings...

### feedparser_pycdas.dis

- `
                        606     LOAD_FAST                       7: boundary
                       ...`
- `
                80      MAKE_FUNCTION                   0
                82      STORE_NAME       ...`
- `,)
                        34      IMPORT_NAME                     3: email.message
                ...`
- `
                48      MAKE_FUNCTION                   0
                50      STORE_NAME       ...`
- `,)
        24      IMPORT_NAME                     3: email
        26      IMPORT_FROM             ...`
- `,)
        48      IMPORT_NAME                     7: collections
        50      IMPORT_FROM       ...`
- `
        94      CALL_METHOD                     1
        96      STORE_NAME                      1...`
- `
                        300     CALL_FUNCTION                   1
                        302     R...`
- `
                64      MAKE_FUNCTION                   0
                66      STORE_NAME       ...`
- `
        158     CALL_FUNCTION                   2
        160     STORE_NAME                      2...`
- `
                        250     CALL_METHOD                     1
                        252     S...`
- `
        114     CALL_METHOD                     1
        116     STORE_NAME                      1...`
- `
                        164     COMPARE_OP                      2 (==)
                        166 ...`
- `
                        12      COMPARE_OP                      2 (==)
                        14  ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                        2       STORE_FAST                      2: lastheader
                     ...`
- `
                16      MAKE_FUNCTION                   0
                18      STORE_NAME       ...`
- `
        124     STORE_NAME                      18: NL
        126     LOAD_NAME                   ...`
- `
                        962     COMPARE_OP                      2 (==)
                        964 ...`
- `
        74      CALL_METHOD                     1
        76      STORE_NAME                      1...`
- Plus 25 more strings...

### _header_value_parser_pycdas.dis

- `
                208     JUMP_FORWARD                    1 (to 212)
                210     LOAD_FAS...`
- `
                        14      COMPARE_OP                      2 (==)
                        16  ...`
- `
                22      CALL_METHOD                     1
                24      CALL_METHOD      ...`
- `
                14      CALL_METHOD                     2
                16      LOAD_METHOD      ...`
- `
                        16      CALL_METHOD                     1
                        18      P...`
- `
                100     COMPARE_OP                      2 (==)
                102     POP_JUMP_IF_...`
- `,)
                364     CALL_FUNCTION_KW                2
                366     STORE_FAST     ...`
- `
        142     CALL_FUNCTION                   1
        144     BINARY_SUBTRACT                 
...`
- `
                166     COMPARE_OP                      2 (==)
                168     POP_JUMP_IF_...`
- `"
                148     LOAD_METHOD                     4: format
                150     LOAD_CON...`
- `
        950     LOAD_NAME                       33: TokenList
        952     CALL_FUNCTION        ...`
- `
                26      CALL_METHOD                     1
                28      CALL_METHOD      ...`
- `
                84      COMPARE_OP                      2 (==)
                86      POP_JUMP_IF_...`
- `
                364     CALL_FUNCTION                   2
                366     UNPACK_SEQUENCE  ...`
- `
                42      MAKE_FUNCTION                   0
                44      CALL_FUNCTION    ...`
- `
        598     LOAD_NAME                       33: TokenList
        600     CALL_FUNCTION        ...`
- `
        374     LOAD_NAME                       33: TokenList
        376     CALL_FUNCTION        ...`
- `
        342     LOAD_NAME                       34: WhiteSpaceTokenList
        344     CALL_FUNCTI...`
- `
        566     LOAD_NAME                       33: TokenList
        568     CALL_FUNCTION        ...`
- `
                40      COMPARE_OP                      2 (==)
                42      POP_JUMP_IF_...`
- Plus 406 more strings...

### errors_pycdas.dis

- `
        404     LOAD_NAME                       25: HeaderDefect
        406     CALL_FUNCTION     ...`
- `
        292     LOAD_NAME                       11: MessageDefect
        294     CALL_FUNCTION    ...`
- `
        62      LOAD_NAME                       3: MessageParseError
        64      CALL_FUNCTION ...`
- `
        30      LOAD_NAME                       2: MessageError
        32      CALL_FUNCTION      ...`
- `
        224     LOAD_NAME                       11: MessageDefect
        226     CALL_FUNCTION    ...`
- `
        276     LOAD_NAME                       11: MessageDefect
        278     CALL_FUNCTION    ...`
- `
                22      MAKE_FUNCTION                   9
                24      STORE_NAME       ...`
- `
                20      MAKE_FUNCTION                   8
                22      STORE_NAME       ...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `InvalidDateDefect`
- `
        78      LOAD_NAME                       2: MessageError
        80      LOAD_NAME          ...`
- `
        208     LOAD_NAME                       11: MessageDefect
        210     CALL_FUNCTION    ...`
- `
        112     LOAD_NAME                       2: MessageError
        114     CALL_FUNCTION      ...`
- `
        160     LOAD_NAME                       11: MessageDefect
        162     CALL_FUNCTION    ...`
- `
        340     LOAD_NAME                       11: MessageDefect
        342     CALL_FUNCTION    ...`
- `
        356     LOAD_NAME                       25: HeaderDefect
        358     CALL_FUNCTION     ...`
- `
        14      LOAD_NAME                       1: Exception
        16      CALL_FUNCTION         ...`
- `
                        2       LOAD_METHOD                     0: format
                        4...`
- `
        324     LOAD_NAME                       11: MessageDefect
        326     CALL_FUNCTION    ...`
- Plus 15 more strings...

### charset_pycdas.dis

- `
        414     LOAD_CONST                      20: `
- `
                6       STORE_NAME                      2: __qualname__
                8       LOA...`
- `
                68      MAKE_FUNCTION                   0
                70      STORE_NAME       ...`
- `
        366     LOAD_CONST                      16: `
- `
        330     LOAD_CONST                      13: `
- `
                52      MAKE_FUNCTION                   0
                54      STORE_NAME       ...`
- `
                12      CALL_FUNCTION                   1
                14      RAISE_VARARGS    ...`
- `,)
        40      IMPORT_NAME                     4: email
        42      IMPORT_FROM             ...`
- `Charset`
- `
        372     LOAD_CONST                      17: `
- `
                        26      RETURN_VALUE                    
                        28      LO...`
- `)
        454     BUILD_CONST_KEY_MAP             3
        456     STORE_NAME                      ...`
- `
                        8       STORE_FAST                      2: codec
                        10...`
- `
        242     LOAD_NAME                       10: BASE64
        244     LOAD_NAME               ...`
- `
        420     LOAD_CONST                      21: `
- `
        488     MAKE_FUNCTION                   0
        490     STORE_NAME                      2...`
- `)
        4       LIST_EXTEND                     1
        6       STORE_NAME                      ...`
- `
        104     LOAD_NAME                       9: QP
        106     LOAD_NAME                    ...`
- `
                14      LOAD_CONST                      2: `
- `
        278     LOAD_NAME                       10: BASE64
        280     LOAD_CONST              ...`
- Plus 34 more strings...

### iterators_pycdas.dis

- `
        2       STORE_NAME                      0: __doc__
        4       BUILD_LIST              ...`
- `,)
                68      CALL_FUNCTION_KW                2
                70      POP_TOP        ...`
- `
                16      LOAD_FAST                       2: level
                18      LOAD_CONST...`
- `
        46      MAKE_FUNCTION                   1
        48      STORE_NAME                      6...`
- `)
                44      CALL_FUNCTION_KW                3
                46      POP_TOP         ...`
- `,)
                22      CALL_FUNCTION_KW                1
                24      STORE_FAST     ...`
- `,)
        24      IMPORT_NAME                     3: io
        26      IMPORT_FROM                ...`
- `
        56      MAKE_FUNCTION                   1
        58      STORE_NAME                      7...`

### vdict_pycdas.dis

- `
                102     MAKE_FUNCTION                   8
                104     STORE_NAME       ...`
- `
                        4       MAKE_FUNCTION                   0
                        6       L...`
- `
                        14      CALL_FUNCTION                   1
                        16      R...`
- `
        64      MAKE_FUNCTION                   0
        66      LOAD_CONST                      6...`
- `,)
        12      IMPORT_NAME                     1: collections
        14      IMPORT_FROM       ...`
- `
                58      MAKE_FUNCTION                   8
                60      STORE_NAME       ...`
- `
                210     MAKE_FUNCTION                   0
                212     STORE_NAME       ...`
- `
                        50      LOAD_GLOBAL                     5: type
                        52 ...`
- `
        82      MAKE_FUNCTION                   0
        84      LOAD_CONST                      8...`
- `
                160     MAKE_FUNCTION                   0
                162     STORE_NAME       ...`
- `
                22      MAKE_FUNCTION                   0
                24      STORE_NAME       ...`
- `
                        14      CALL_FUNCTION                   1
                        16      R...`
- `
                        42      MAKE_FUNCTION                   8
                        44      S...`
- `
                82      MAKE_FUNCTION                   8
                84      STORE_NAME       ...`
- `
                194     MAKE_FUNCTION                   0
                196     STORE_NAME       ...`
- `
        116     STORE_NAME                      4: _iter_values
        118     LOAD_NAME          ...`
- `
                178     MAKE_FUNCTION                   1
                180     STORE_NAME       ...`
- `
        100     MAKE_FUNCTION                   0
        102     LOAD_CONST                      1...`
- `
                        68      CALL_FUNCTION                   1
                        70      R...`
- `
                226     MAKE_FUNCTION                   0
                228     STORE_NAME       ...`
- Plus 15 more strings...

