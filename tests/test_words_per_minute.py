from lib.words_per_minute import *

def test_200_words_string():
    str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla at convallis lectus. Cras fermentum nec dui vel molestie. Aenean feugiat lorem non libero ultrices, in volutpat est mattis. Sed eu ipsum sagittis, sagittis elit ut, mattis ante. Nunc dolor magna, lobortis nec semper ut, rutrum non ex. Sed in volutpat ex. Quisque eu risus vel diam porttitor sodales. Curabitur a mattis augue. Nulla cursus augue vitae risus viverra, at imperdiet sapien dapibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum eu fermentum turpis. Etiam sit amet urna efficitur, sagittis lacus at, tempus odio. Fusce iaculis arcu eu est fringilla consequat. Donec convallis lacinia metus non ornare. Duis volutpat turpis purus, id dapibus enim varius ut. Praesent ut massa quis risus varius ullamcorper. Quisque velit leo, imperdiet vel convallis id, dapibus sodales odio. Nulla vitae auctor tellus, non bibendum ligula. Vivamus convallis, nulla sed luctus ultricies, tortor libero pulvinar nunc, ut auctor arcu arcu eu eros. Quisque quis nunc purus. Mauris nec tellus ex. Morbi viverra commodo convallis. In ut consectetur enim. Vivamus tincidunt enim vitae lacinia condimentum. Cras eu mollis lacus. Sed non mi ut orci dignissim suscipit. Quisque suscipit posuere ligula id porta."
    result = words_per_minute(str)
    assert result == 1

def test_400_words_string():
    str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent viverra varius accumsan. Donec diam odio, gravida sed nisi vel, vulputate laoreet dui. Praesent non blandit ipsum. Aliquam iaculis a enim a consectetur. Donec non rutrum orci. Vivamus pretium velit eget nulla bibendum, vel ultrices diam tincidunt. Donec nec ipsum laoreet lorem auctor fringilla et dignissim orci. In nulla sem, mattis sit amet nisi et, porta tempor quam. Etiam suscipit, mauris et consequat cursus, dolor velit elementum leo, quis vestibulum ligula felis non mauris. Nullam eget leo malesuada, luctus nibh vel, vulputate quam. Duis rhoncus porttitor mauris quis porttitor. Sed sodales feugiat elementum. Sed vehicula in mi et facilisis. Etiam imperdiet erat a tincidunt interdum. Nunc ut neque nec purus gravida cursus. Nunc bibendum, risus at faucibus sollicitudin, purus orci molestie mi, vitae congue enim nibh sed sapien. Proin eu diam sit amet urna tristique elementum ut ut ipsum. Nulla dapibus, sem non ornare commodo, odio quam accumsan nisi, eget facilisis neque nunc nec lacus. Pellentesque commodo auctor accumsan. Donec non vestibulum dolor, eu sagittis urna. Sed finibus mattis libero, eu interdum nisl consequat at. Nam eu ex quis mauris tempus ultrices ut eu dui. Cras ex diam, mattis et eros quis, rhoncus luctus nisl. Vivamus et eros id risus tincidunt suscipit posuere et massa. Nullam tincidunt a nulla eu lobortis. Donec tempus efficitur urna nec iaculis. Sed lobortis massa nec accumsan viverra. Duis consectetur eget dolor quis hendrerit. Praesent ac libero iaculis, elementum risus in, faucibus magna. Proin sapien sem, vehicula id vestibulum in, imperdiet lacinia lectus. Cras nec finibus leo. Pellentesque sem magna, convallis nec vulputate in, dictum sit amet libero. Etiam malesuada est sed rhoncus posuere. Proin in tellus sed mi tempor molestie non vel lorem. Etiam vel mauris dictum, commodo justo bibendum, semper nisl. Mauris maximus arcu vitae lorem aliquet, eget varius tellus vulputate. Cras accumsan risus quis leo vulputate, sagittis euismod est bibendum. Praesent quis rutrum eros. Fusce mollis, ante in semper dapibus, metus nunc eleifend nisi, in vehicula libero arcu sed enim. Vivamus nibh eros, dictum vel metus vel, imperdiet dictum quam. Donec ac nisi eget neque laoreet tincidunt. Curabitur aliquam, nibh nec euismod egestas, metus enim luctus orci, in scelerisque neque velit in risus. Sed elit nibh, varius at lorem vitae, cursus varius sem. Ut ultricies sapien ac sem mollis cursus. Praesent purus felis, congue sit amet ultricies at, feugiat ut ante. Etiam interdum."
    result = words_per_minute(str)
    assert result == 2

def test_100_words_string():
    str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur pulvinar id metus id dapibus. Etiam imperdiet, tellus sit amet cursus pharetra, magna justo venenatis felis, sed iaculis tellus lectus vitae mi. Nullam condimentum mi libero, vitae bibendum velit rutrum vitae. In non varius mauris, nec consequat augue. Aliquam dignissim mi vel risus imperdiet accumsan. Vestibulum ut urna vel metus venenatis blandit ut scelerisque mi. Nunc vestibulum sit amet dui nec consequat. Sed fringilla ante tortor. In eget elit ac libero accumsan mattis ut at nibh. Fusce mollis, ligula eget tristique finibus, enim risus auctor nunc, vel tempus ligula ex ut."
    result = words_per_minute(str)
    assert result == 0.5