# https://leetcode.com/problems/longest-duplicate-substring/
# 1044. Longest Duplicate Substring


class Solution:
    base = 40999999
    modulus = 999999937

    def rabin_karp(
        self, s: str, patterns: set[str], pattern_len: int, h: int
    ) -> tuple[str, bool]:
        h = pow(self.base, pattern_len - 1) % self.modulus
        pattern_hashes: set[int] = set()
        for pattern in patterns:
            pattern_hash = 0
            for char in pattern:
                pattern_hash = (self.base * pattern_hash + ord(char)) % self.modulus
            pattern_hashes.add(pattern_hash)
        next_hash = 0
        for i in range(pattern_len):
            next_hash = (self.base * next_hash + ord(s[i])) % self.modulus
        s_len = len(s)
        patterns_count = {pattern: 0 for pattern in patterns}
        for i in range(s_len - pattern_len + 1):
            substring = s[i : i + pattern_len]
            if next_hash in pattern_hashes and substring in patterns:
                patterns_count[substring] += 1
                if patterns_count[substring] == 2:
                    return substring, True
            if i < s_len - pattern_len:
                next_hash = (
                    next_hash - h * ord(s[i])
                ) % self.modulus  # remove letter i
                next_hash = (
                    next_hash * self.base + ord(s[i + pattern_len])
                ) % self.modulus  # add letter i + pattern_len
                next_hash = (
                    next_hash + self.modulus
                ) % self.modulus  # make sure that next_hash >= 0
        return "", False

    def longestDupSubstring(self, s: str) -> str:  # noqa: N802
        s_len = len(s)
        pattern_len = s_len // 2
        lower = 1
        upper = s_len
        pattern = ""
        while lower != upper:
            substrings: set[str] = set()
            for i in range(s_len - pattern_len + 1):
                substrings.add(s[i : i + pattern_len])
            new_pattern, found_dup = self.rabin_karp(
                s,
                substrings,
                pattern_len,
                pow(self.base, pattern_len - 1) % self.modulus,
            )
            if not found_dup:
                upper = pattern_len
            else:
                pattern = new_pattern
                lower = pattern_len + 1
            pattern_len = (upper + lower) // 2
        return pattern


solution = Solution()


s = "banana"
assert solution.longestDupSubstring(s) == "ana"

s = "abcd"
assert solution.longestDupSubstring(s) == ""

s = "nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"
print(solution.longestDupSubstring(s))

s = "rtbbfywifhhthadpjixdeodqfgjfykvjwagudthnwfjdqyfskgczdzdsomkxfeizyfnmkirnklfevunbwvevymyoxcnddzhrqnengvjrptpgkusjfpcivknmpcptgbkosyujjcpqugnizpfqfxzrpyxmtbvpxqfbrrupmppkxyltyumcxtyefxjqlmpfymxvrbjmxvqtgnorweoujekkbpdzvhzvchdslcbmavwmjnlypoexhqoxfrnglcyhetrhpemrryhoanasaoyfxeznfeqkgqkzxcuphvngwryfouyugtrhxjfkegzgypucmpanrgyourwglemiclqkcubxbjzhkqzqextijwbfyizgylkyjxeuulkurebpovcxklywnwflnvmufbaauloekgtnabkvfvlsghtgqrkvopcablizoqdcxomhhyxtuwdebmjihmchdxtklvdecwvgogwwepqowfuwluklfiibyqaikphnfpfzhralzuuhsptonslvmkfojfdsumnwwacfwqxkotcqewulorinpzmhduhriisuajcpwjeanvyvpyefglpmfcicsglxtwadtrtaxnozxvchwagdyyinhqmhofuknauhwkinwzmrmermnnzndaxmqkgzotjgkxqhfqvgnvzymvcmdqpfiixrkmjpdbelzojbjeublnwcdsckbpwbbwlloxhecimaysjzwbppgmzywbouicyjdcsaffcxxkmwoamjzicswfzhccdlzewmzotyzprhreseqgmafkzkjqzwukrunckowdfajqhyrhhfhjfuzhvwgkwrmmpgribxqchowwvlbppnkofdfdennafqzawkycytghxehrjwdbrgroqfyoxynkketzkmglrsbqaxgfbiwhtuhzlpszsgbybawnguqhyadwteiikbahnhqdpvmobcsozloyyopxsnjlbgisytssbjbbuucqyvobnflnxtd"
print(solution.longestDupSubstring(s))

s = "unuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczxunuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczx"
print(solution.longestDupSubstring(s))
