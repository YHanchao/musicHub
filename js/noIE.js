function isIE()
{
    if (!!window.ActiveXObject || "ActiveXObject" in window)
    {
        alert("不支持IE浏览器");
        window.close();
    }
}
isIE();