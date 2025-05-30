# Classes by Module

## .py

- `AddrlistClass`
- `AddressList (AddrlistClass)`

## _adapters

- `Message (email.message.Message)`
  - Methods:
    - `redent(value)`
    - `transform(key = None)`

## _bootstrap

- `_DeadlockError (RuntimeError)`
- `_ModuleLock`
- `_DummyModuleLock`
- `_ModuleLockManager`
- `ModuleSpec`
- `BuiltinImporter`
- `FrozenImporter`
- `_ImportLockContext`

## _collections

- `FreezableDefaultDict (collections.defaultdict)`

## _compression

- `BaseStream (io.BufferedIOBase)`
- `DecompressReader (io.RawIOBase)`

## _encoded_words

- `_QByteMap (dict)`

## _header_value_parser

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
- `AddressList (TokenList)`
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
- `_InvalidEwError (errors.HeaderParseError)`

## _meta

- `PackageMetadata (Protocol)`
- `SimplePath (Protocol)`

## _parseaddr

- `AddrlistClass`
- `AddressList (AddrlistClass)`

## _policybase

- `_PolicyBase`

## _py_abc

- `ABCMeta (type)`

## _strptime

- `LocaleTime (object)`
- `TimeRE (dict)`

## _text

- `FoldedCase (str)`

## _threading_local

- `_localimpl`
  - Methods:
    - `local_deleted(_ = None, key = None)`
    - `thread_deleted(_ = None, idt = None)`
- `local`

## bz2

- `BZ2File (_compression.BaseStream)`

## calendar

- `IllegalMonthError (ValueError)`
- `IllegalWeekdayError (ValueError)`
- `_localized_month`
- `_localized_day`
- `Calendar (object)`
- `TextCalendar (Calendar)`
- `HTMLCalendar (Calendar)`
- `different_locale`
- `LocaleTextCalendar (TextCalendar)`
- `LocaleHTMLCalendar (HTMLCalendar)`

## contentmanager

- `ContentManager`

## contextlib

- `AbstractContextManager (abc.ABC)`
  - Methods:
    - `inner(*args, **kwds)`
    - `some_generator(<arguments>)`
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `AbstractAsyncContextManager (abc.ABC)`
  - Methods:
    - `inner(*args, **kwds)`
    - `some_generator(<arguments>)`
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `ContextDecorator (object)`
  - Methods:
    - `inner(*args, **kwds)`
    - `some_generator(<arguments>)`
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `AsyncContextDecorator (object)`
  - Methods:
    - `some_generator(<arguments>)`
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `_GeneratorContextManagerBase`
  - Methods:
    - `some_generator(<arguments>)`
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `_GeneratorContextManager (ContextDecorator, AbstractContextManager, _GeneratorContextManagerBase)`
  - Methods:
    - `some_generator(<arguments>)`
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `_AsyncGeneratorContextManager (AsyncContextDecorator, AbstractAsyncContextManager, _GeneratorContextManagerBase)`
  - Methods:
    - `some_generator(<arguments>)`
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `closing (AbstractContextManager)`
  - Methods:
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `aclosing (AbstractAsyncContextManager)`
  - Methods:
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `_RedirectStream (AbstractContextManager)`
  - Methods:
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `redirect_stdout (_RedirectStream)`
  - Methods:
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `redirect_stderr (_RedirectStream)`
  - Methods:
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `suppress (AbstractContextManager)`
  - Methods:
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `_BaseExitStack`
  - Methods:
    - `_exit_wrapper(exc_type = None, exc = None, tb = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `ExitStack (AbstractContextManager, _BaseExitStack)`
  - Methods:
    - `_fix_exception_context(new_exc = None, old_exc = None)`
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `AsyncExitStack (AbstractAsyncContextManager, _BaseExitStack)`
  - Methods:
    - `_fix_exception_context(new_exc = None, old_exc = None)`
- `nullcontext (AbstractAsyncContextManager, AbstractContextManager)`

## copy

- `Error (Exception)`

## csv

- `Dialect`
- `excel (Dialect)`
- `excel_tab (excel)`
- `unix_dialect (Dialect)`
- `DictReader`
- `DictWriter`

## dataclasses

- `FrozenInstanceError (AttributeError)`
- `_HAS_DEFAULT_FACTORY_CLASS`
- `_MISSING_TYPE`
- `_KW_ONLY_TYPE`
- `_FIELD_BASE`
- `InitVar`
- `Field`
- `_DataclassParams`

## dis

- `Instruction (_Instruction)`
- `Bytecode`

## errors

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

## feedparser

- `BufferedSubFile (object)`
- `FeedParser`
- `BytesFeedParser (FeedParser)`

## fractions

- `Fraction (numbers.Rational)`
  - Methods:
    - `__add__(self, other)`
    - `__radd__(self, other)`
    - `forward(a = None, b = None)`
    - `reverse(b = None, a = None)`

## generator

- `Generator`
- `BytesGenerator (Generator)`
- `DecodedGenerator (Generator)`

## gzip

- `_PaddedFile`
- `BadGzipFile (OSError)`
- `GzipFile (_compression.BaseStream)`
- `_GzipReader (_compression.DecompressReader)`

## header

- `Header`
- `_ValueFormatter`
- `_Accumulator (list)`

## headerregistry

- `Address`
- `Group`
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

## install

- `Style`
- `UI`

## ipaddress

- `AddressValueError (ValueError)`
- `NetmaskValueError (ValueError)`
- `_IPAddressBase`
- `_BaseV4`

## lzma

- `LZMAFile (_compression.BaseStream)`

## numbers

- `Complex (Number)`
- `Real (Complex)`
- `Rational (Real)`
- `Integral (Rational)`

## parse

- `_ResultMixinStr (object)`
- `_ResultMixinBytes (object)`
- `_NetlocResultMixinBase (object)`
- `_NetlocResultMixinStr (_ResultMixinStr, _NetlocResultMixinBase)`
- `_NetlocResultMixinBytes (_ResultMixinBytes, _NetlocResultMixinBase)`
- `DefragResult (_ResultMixinStr, _DefragResultBase)`
- `SplitResult (_NetlocResultMixinStr, _SplitResultBase)`
- `ParseResult (_NetlocResultMixinStr, _ParseResultBase)`
- `DefragResultBytes (_ResultMixinBytes, _DefragResultBase)`
- `SplitResultBytes (_NetlocResultMixinBytes, _SplitResultBase)`
- `ParseResultBytes (_NetlocResultMixinBytes, _ParseResultBase)`
- `Quoter (collections.defaultdict)`

## parser

- `Parser`
- `HeaderParser (Parser)`
- `BytesParser`
- `BytesHeaderParser (BytesParser)`

## pathlib

- `_Flavour (object)`
  - Methods:
    - `link(self, src, dst)`
    - `readlink(self, path)`
    - `check_eloop(e)`
- `_WindowsFlavour (_Flavour)`
  - Methods:
    - `link(self, src, dst)`
    - `readlink(self, path)`
    - `check_eloop(e)`
- `_PosixFlavour (_Flavour)`
  - Methods:
    - `link(self, src, dst)`
    - `readlink(self, path)`
    - `check_eloop(e)`
- `_Accessor`
  - Methods:
    - `link(self, src, dst)`
    - `readlink(self, path)`
    - `check_eloop(e)`
- `_NormalAccessor (_Accessor)`
  - Methods:
    - `link(self, src, dst)`
    - `readlink(self, path)`
    - `check_eloop(e)`
- `_Selector`
  - Methods:
    - `check_eloop(e)`
- `_TerminatingSelector`
  - Methods:
    - `check_eloop(e)`
- `_PreciseSelector (_Selector)`
  - Methods:
    - `check_eloop(e)`
- `_WildcardSelector (_Selector)`
  - Methods:
    - `check_eloop(e)`
- `_RecursiveWildcardSelector (_Selector)`
  - Methods:
    - `check_eloop(e)`
- `_PathParents (Sequence)`
  - Methods:
    - `check_eloop(e)`
- `PurePath (object)`
  - Methods:
    - `check_eloop(e)`
- `PurePosixPath (PurePath)`
  - Methods:
    - `check_eloop(e)`
- `PureWindowsPath (PurePath)`
  - Methods:
    - `check_eloop(e)`
- `Path (PurePath)`
  - Methods:
    - `check_eloop(e)`

## pprint

- `_safe_key`
- `PrettyPrinter`

## py_compile

- `PyCompileError (Exception)`
- `PycInvalidationMode (enum.Enum)`

## readers

- `FileReader (abc.TraversableResources)`
- `ZipReader (abc.TraversableResources)`
- `MultiplexedPath (abc.Traversable)`
- `NamespaceReader (abc.TraversableResources)`

## selectors

- `_SelectorMapping (Mapping)`

## shlex

- `shlex`

## statistics

- `StatisticsError (ValueError)`

## string

- `Template`
  - Methods:
    - `convert(mo = None)`
    - `convert(mo = None)`
- `Formatter`

## textwrap

- `TextWrapper`
  - Methods:
    - `predicate(line)`

## tracemalloc

- `Statistic`
- `StatisticDiff`
- `Trace`
- `_Traces (Sequence)`
- `BaseFilter`
- `Filter (BaseFilter)`
- `DomainFilter (BaseFilter)`
- `Snapshot`

## translate

- `Translate`

## ttk

- `Style (object)`
  - Methods:
    - `adjust_label()`
- `Widget (tkinter.Widget)`
  - Methods:
    - `adjust_label()`
- `Button (Widget)`
  - Methods:
    - `adjust_label()`
- `Checkbutton (Widget)`
  - Methods:
    - `adjust_label()`
- `Entry (tkinter.Entry, Widget)`
  - Methods:
    - `adjust_label()`
- `Combobox (Entry)`
  - Methods:
    - `adjust_label()`
- `Frame (Widget)`
  - Methods:
    - `adjust_label()`
- `Label (Widget)`
  - Methods:
    - `adjust_label()`
- `Labelframe (Widget)`
  - Methods:
    - `adjust_label()`
- `Menubutton (Widget)`
  - Methods:
    - `adjust_label()`
- `Notebook (Widget)`
  - Methods:
    - `adjust_label()`
- `Panedwindow (tkinter.PanedWindow, Widget)`
  - Methods:
    - `adjust_label()`
- `Progressbar (Widget)`
  - Methods:
    - `adjust_label()`
- `Radiobutton (Widget)`
  - Methods:
    - `adjust_label()`
- `Scale (tkinter.Scale, Widget)`
  - Methods:
    - `adjust_label()`
- `Scrollbar (tkinter.Scrollbar, Widget)`
  - Methods:
    - `adjust_label()`
- `Separator (Widget)`
  - Methods:
    - `adjust_label()`
- `Sizegrip (Widget)`
  - Methods:
    - `adjust_label()`
- `Spinbox (Entry)`
  - Methods:
    - `adjust_label()`
- `Treeview (tkinter.YView, tkinter.XView, Widget)`
  - Methods:
    - `adjust_label()`
- `LabeledScale (Frame)`
  - Methods:
    - `adjust_label()`
- `OptionMenu (Menubutton)`

## typing

- `_Final`
- `_Immutable`
- `Starship`
- `Connection`
- `FastConnector (Connection)`

## uu

- `Error (Exception)`

## vdict

- `_kView (_c.KeysView)`
  - Methods:
    - `dict_recurse(obj = None)`
- `_vView (_c.ValuesView)`
  - Methods:
    - `dict_recurse(obj = None)`
- `_iView (_c.ItemsView)`
  - Methods:
    - `dict_recurse(obj = None)`
- `VDFDict (dict)`

## webbrowser

- `Error (Exception)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `BaseBrowser (object)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `GenericBrowser (BaseBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `BackgroundBrowser (GenericBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `UnixBrowser (BaseBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Mozilla (UnixBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Netscape (UnixBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Galeon (UnixBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Chrome (UnixBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Opera (UnixBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Elinks (UnixBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Konqueror (BaseBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `Grail (BaseBrowser)`
  - Methods:
    - `__init__(self, name)`
    - `__init__(self, name)`
- `WindowsDefault (BaseBrowser)`
- `MacOSX (BaseBrowser)`
- `MacOSXOSAScript (BaseBrowser)`

