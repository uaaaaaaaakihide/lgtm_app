import click
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image
@click.command()
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='Oracle画像です')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm') # 動作確認用

def lgtm(keyword, message):
    # ここにロジックを追加していく
    # pass
    with get_image(keyword) as fp:
        save_with_message(fp, message)
