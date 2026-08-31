from collective.contentsections.sections.base import SectionView


class TextSectionView(SectionView):
    """TextSection view"""

    @property
    def lead_image_scale(self):
        width = self.context.lead_image_width
        match width:
            case 3:
                return "preview"
            case 4:
                return "teaser"
            case 6:
                return "large"
            case 8 | 9:
                return "larger"
            case 12:
                return "huge"
        return "mini"
